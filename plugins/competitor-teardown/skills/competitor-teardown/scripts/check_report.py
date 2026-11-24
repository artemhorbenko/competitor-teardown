#!/usr/bin/env python3
"""Render-check a competitor-teardown report in a headless browser.

Usage:
    python check_report.py report.html [--out ./report-check] [--browser /path/to/chrome]

Opens the page as desktop (1280px), tablet (820px, touch) and phone (390px, touch),
runs the checks from SKILL.md step 7, saves screenshots and prints a summary.
Exit code 0 = all checks passed, 1 = something failed, 2 = could not run.

Needs: pip install playwright && playwright install chromium
(or pass --browser with the path to an installed Chrome/Chromium).
"""
import argparse
import asyncio
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

VIEWS = [
    ("desktop", dict(viewport={"width": 1280, "height": 900})),
    ("tablet", dict(viewport={"width": 820, "height": 1100}, is_mobile=True, has_touch=True)),
    ("phone", dict(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=2)),
]

# Returns a dict of simple facts about the rendered page.
PROBE = """() => {
  const q = s => document.querySelector(s);
  const svgKids = s => { const e = q(s + ' svg'); return e ? e.childElementCount : 0; };
  const tds = sel => [...document.querySelectorAll(sel + ' td')];
  const bad = sel => tds(sel).filter(td => !(td.children.length === 1 && td.firstElementChild.classList.contains('cv'))).length;
  const ids = new Set([...document.querySelectorAll('.srcs li')].map(li => '#' + li.id));
  const svgText = sel => [...document.querySelectorAll(sel + ' svg text')].filter(t => t.textContent.trim() && t.getBBox().width > 0);
  const clash = list => { let n = 0; const r = list.map(t => t.getBoundingClientRect());
    for (let i = 0; i < r.length; i++) for (let j = i + 1; j < r.length; j++) { const a = r[i], b = r[j];
      if (a.left < b.right - 2 && b.left < a.right - 2 && a.top < b.bottom - 2 && b.top < a.bottom - 2) n++; } return n; };
  const outside = (sel) => { const box = q(sel); if (!box) return 0; const B = box.getBoundingClientRect();
    return svgText(sel).filter(t => { const r = t.getBoundingClientRect(); return r.left < B.left - 2 || r.right > B.right + 2 || r.top < B.top - 2 || r.bottom > B.bottom + 2; }).length; };
  return {
    scrollWidth: document.documentElement.scrollWidth,
    width: innerWidth,
    canvas: svgKids('#cv'),
    map: svgKids('#pm'),
    matrix: svgKids('#mx'),
    canvasLines: document.querySelectorAll('#cv polyline').length,
    products: document.querySelectorAll('#prods .prod').length,
    kpis: [...document.querySelectorAll('#kpis .num')].filter(n => n.textContent.trim()).length,
    cmpRows: document.querySelectorAll('#cmpBody tr:not(.grp)').length,
    rows: document.querySelectorAll('#tbody tr').length,
    errc: document.querySelectorAll('#errcGrid .eb').length,
    win: document.querySelectorAll('#winList article, #loseList article').length,
    badCells: bad('#cmpBody') + bad('#tbody'),
    deadRefs: [...document.querySelectorAll('.sref')].filter(a => !ids.has(a.getAttribute('href'))).length,
    refs: document.querySelectorAll('#cmpBody .sref').length,
    tableTerms: document.querySelectorAll('#tbody .t, #cmpBody .t').length,
    terms: document.querySelectorAll('.t').length,
    mapClash: clash(svgText('#pm').filter(t => t.getAttribute('font-weight') >= 600)),
    canvasClash: clash(svgText('#cv')),
    outside: outside('#cv') + outside('#pm'),
    overflows: [...document.querySelectorAll('.kpi small, .kpi .num, .card h3, .prod b, .eb li, .wl article h3, .cmp th')].filter(e => e.offsetParent && e.scrollWidth > e.clientWidth + 2).length,
  };
}"""

TIP_VISIBLE = "() => !!document.getElementById('tip') && getComputedStyle(document.getElementById('tip')).display !== 'none'"


def script_check(html: str):
    """Return an error string if the last <script> does not parse (needs node)."""
    node = shutil.which("node")
    if not node or "<script>" not in html:
        return None
    src = html[html.rindex("<script>") + 8: html.rindex("</script>")]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(src)
    r = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
    return None if r.returncode == 0 else r.stderr.strip().splitlines()[-1]


async def shot(page, out, name, sel):
    if await page.query_selector(sel):
        await page.evaluate(f"document.querySelector('{sel}').scrollIntoView()")
        await page.wait_for_timeout(250)
        await page.screenshot(path=str(out / name))


async def check_view(browser, url, name, ctx_args, out):
    fails, notes = [], []
    ctx = await browser.new_context(**ctx_args)
    page = await ctx.new_page()
    errors = []
    page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    page.on("console", lambda m: errors.append(f"console: {m.text}") if m.type == "error" and "fonts" not in m.text else None)
    await page.goto(url)
    await page.wait_for_timeout(1500)
    p = await page.evaluate(PROBE)

    if p["scrollWidth"] > p["width"] + 1:
        fails.append(f"sideways scroll: page is {p['scrollWidth']}px wide in a {p['width']}px viewport")
    for key, label in [("canvas", "strategy canvas"), ("map", "positioning map"), ("matrix", "impact-effort matrix")]:
        if not p[key]:
            fails.append(f"{label} is empty")
    if p["canvasLines"] != p["products"]:
        fails.append(f"strategy canvas has {p['canvasLines']} lines for {p['products']} products")
    if not p["kpis"]:
        fails.append("KPI row has no numbers")
    if not p["cmpRows"]:
        fails.append("comparison matrix is empty")
    if not p["rows"]:
        fails.append("moves table is empty")
    if p["errc"] != 4:
        fails.append("ERRC grid does not have 4 boxes")
    if not p["win"]:
        notes.append("win / lose lists are empty")
    if p["badCells"]:
        fails.append(f"{p['badCells']} table cells are not wrapped in one .cv (breaks the phone layout)")
    if p["deadRefs"]:
        fails.append(f"{p['deadRefs']} source links point to no source in the list")
    if not p["refs"]:
        fails.append("comparison matrix cells show no source numbers")
    if p["mapClash"]:
        fails.append(f"{p['mapClash']} overlapping product labels on the positioning map")
    if p["canvasClash"]:
        fails.append(f"{p['canvasClash']} overlapping labels on the strategy canvas")
    if p["outside"]:
        fails.append(f"{p['outside']} chart labels are cut off at the chart edge")
    if p["overflows"]:
        fails.append(f"{p['overflows']} labels overflow their box")
    if not p["terms"]:
        notes.append("no tooltip terms found (.t)")

    await page.screenshot(path=str(out / f"{name}-top.png"))

    term = await page.query_selector("#cmpBody .t") or await page.query_selector("#ops .t") or await page.query_selector(".t")
    if term:
        await term.scroll_into_view_if_needed()
        await page.wait_for_timeout(200)
        if name == "desktop":
            await term.hover()
        else:
            await term.tap()
        await page.wait_for_timeout(250)
        if not await page.evaluate(TIP_VISIBLE):
            fails.append("tooltip does not open on " + ("hover" if name == "desktop" else "tap"))
        else:
            await page.screenshot(path=str(out / f"{name}-tooltip.png"))
            if name != "desktop":
                await term.tap()
                await page.wait_for_timeout(250)
                if await page.evaluate(TIP_VISIBLE):
                    fails.append("tooltip does not close on a second tap")

    # Filters on both tables: cells and tooltips must survive a re-render.
    for sel, attr in (("#matrix .chip[data-m]", "data-m"), ("#ops .chip[data-f]", "data-f")):
        chips = await page.query_selector_all(sel)
        for chip in chips:
            f = await chip.get_attribute(attr)
            await chip.click()
            await page.wait_for_timeout(200)
            p2 = await page.evaluate(PROBE)
            if f == "all" and (p2["rows"] == 0 or p2["cmpRows"] == 0):
                fails.append(f"filter 'all' ({sel}) leaves a table empty")
            if p2["badCells"]:
                fails.append(f"after filter '{f}' table cells lose their .cv wrapper")
            if p2["deadRefs"]:
                fails.append(f"after filter '{f}' source links break")
            if f == "all" and p["tableTerms"] and p2["tableTerms"] == 0:
                fails.append("tooltips disappear from the tables after filtering")
        if chips:
            await chips[0].click()
            await page.wait_for_timeout(200)

    for sel, label in [("#matrix", "matrix"), ("#canvas", "canvas"), ("#errc", "errc-map"), ("#win", "win-lose"), ("#ops", "moves"), ("#plan", "plan"), ("#data", "sources")]:
        await shot(page, out, f"{name}-{label}.png", sel)

    if name == "phone":
        await page.emulate_media(color_scheme="dark")
        await page.evaluate("scrollTo(0,0)")
        await page.wait_for_timeout(300)
        await page.screenshot(path=str(out / "phone-dark.png"))
        await shot(page, out, "phone-dark-matrix.png", "#matrix")

    fails += errors
    await ctx.close()
    return {"view": name, "ok": not fails, "fails": fails, "notes": notes, "facts": p}


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--out", default="report-check")
    ap.add_argument("--browser", help="path to Chrome/Chromium if Playwright's own is not installed")
    a = ap.parse_args()

    path = pathlib.Path(a.report).resolve()
    if not path.exists():
        print(f"not found: {path}")
        return 2
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    results = []
    err = script_check(path.read_text(encoding="utf-8"))
    if err:
        results.append({"view": "script", "ok": False, "fails": [f"script does not parse: {err}"]})

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("playwright is not installed: pip install playwright && playwright install chromium")
        return 2

    async with async_playwright() as pw:
        launch = {"args": ["--no-sandbox"]}
        exe = a.browser or next((shutil.which(b) for b in ("google-chrome", "chromium", "chromium-browser") if shutil.which(b)), None)
        try:
            browser = await pw.chromium.launch(**launch)
        except Exception:
            if not exe:
                print("no browser: run `playwright install chromium` or pass --browser")
                return 2
            browser = await pw.chromium.launch(executable_path=exe, **launch)
        for name, ctx_args in VIEWS:
            results.append(await check_view(browser, path.as_uri(), name, ctx_args, out))
        await browser.close()

    ok = all(r["ok"] for r in results)
    for r in results:
        print(f"[{'PASS' if r['ok'] else 'FAIL'}] {r['view']}")
        for f in r.get("fails", []):
            print(f"   - {f}")
        for n in r.get("notes", []):
            print(f"   note: {n}")
    print(f"screenshots: {out.resolve()}")
    (out / "result.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
