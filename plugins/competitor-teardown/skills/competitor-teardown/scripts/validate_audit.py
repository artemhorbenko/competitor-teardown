#!/usr/bin/env python3
"""Check a competitor-teardown audit.json before it becomes a report.

Usage: python validate_audit.py audit.json [--today YYYY-MM-DD]

Errors (exit 1) break the report or the skill's rules; warnings (exit 0)
are worth a look. Standard library only.

Rules checked beyond the shape:
- every matrix cell exists for every product; a cell with a value cites a
  source that has a URL and a checked-on date and is not marked "no";
- a cell or evidence item about product P that cites another vendor's page
  (kind own/rival, by != P) must be marked claim: true;
- quotes ("...", “...”, «...») are at most 15 words;
- every move has competitor evidence with sources; the top 3 have a plan,
  alternatives, risk type, threshold and pre-mortem;
- KPI numbers name a source; win/lose items cite sources.
"""
import datetime
import json
import re
import sys

LENSES = {"pos", "buyer", "breadth", "price", "proof", "attack", "onb", "integ", "rev", "seo", "sig", "chg"}
AREAS = {"page", "message", "pricing", "feature", "content", "proof", "sales", "data"}
KINDS = {"own", "rival", "review", "third", "data", "owner", "tool"}
VALUES = {"yes", "part", "no", "nd"}
LANGS = {"uk", "en"}
STATUSES = {"ok", "demo", "no"}
TOKENS = re.compile(r"\{(lead|trail|crit|cells|qw|n|conf)\}")
TEXT_KEYS = ["headline", "lead", "matrixH", "canvasH", "errcH", "mapH", "winH", "mxH", "opsH", "nextH", "planH", "dataH"]
QUOTES = re.compile(r'"([^"]+)"|“([^”]+)”|«([^»]+)»')
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MAX_QUOTE = 15


def strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for i, x in enumerate(o):
            yield from strings(x, f"{path}[{i}]")
    elif isinstance(o, dict):
        for k, x in o.items():
            yield from strings(x, f"{path}.{k}" if path else k)


def validate(a, today=None):
    err, warn = [], []
    E, W = err.append, warn.append
    if not isinstance(a, dict):
        return ["the file is not a JSON object"], []
    today = today or datetime.date.today().isoformat()

    if a.get("lang") not in LANGS:
        W(f"lang '{a.get('lang')}' has no interface dictionary; labels fall back to English")
    text = a.get("text") or {}
    for k in TEXT_KEYS:
        if not str(text.get(k, "")).strip():
            E(f"text.{k} is missing: every section needs a heading that states its point")
    if "<" in json.dumps(text, ensure_ascii=False):
        W("text contains '<': HTML is shown as plain text; use [[...]] to highlight words")

    # sources
    sources = a.get("sources") or []
    src = {}
    if not sources:
        E("sources is empty: list every page, listing and tool used, and what was missing")
    for i, s in enumerate(sources):
        p = f"sources[{i}]"
        sid = s.get("id")
        if not sid:
            E(f"{p}.id is missing")
            continue
        if sid in src:
            E(f"{p}.id '{sid}' is used twice")
        src[sid] = s
        if s.get("status") not in STATUSES:
            E(f"{p}.status must be ok, demo or no")
        if s.get("kind") not in KINDS:
            E(f"{p}.kind must be one of {', '.join(sorted(KINDS))}")
        if not s.get("name"):
            E(f"{p}.name is missing")
        if s.get("url"):
            d = s.get("date", "")
            if not DATE.match(str(d)):
                E(f"{p} '{sid}' has a url but no checked-on date (YYYY-MM-DD)")
            elif d > today:
                E(f"{p} '{sid}' date {d} is in the future")
        if s.get("kind") in ("own", "rival") and not s.get("by"):
            E(f"{p} '{sid}' is kind {s.get('kind')}: set by = the product id of the vendor who published it")

    def usable(sid, where):
        s = src.get(sid)
        if not sid:
            E(f"{where} cites no source")
            return None
        if not s:
            E(f"{where} cites '{sid}', which is not in sources")
            return None
        if s.get("status") == "no":
            E(f"{where} cites '{sid}', which is marked as not available")
        if s.get("kind") not in ("owner", "data", "tool") and not s.get("url"):
            E(f"{where} cites '{sid}', which has no url")
        return s

    def claim_ok(s, pid, claim, where):
        if s and s.get("kind") in ("own", "rival") and s.get("by") and s["by"] != pid and not claim:
            E(f"{where} is about '{pid}' but cites a page by '{s['by']}': mark it claim: true (one vendor's words about another are a claim, not a fact)")

    # products
    prods = a.get("products") or []
    pids = [p.get("id") for p in prods]
    if not 2 <= len(prods) <= 6:
        E(f"products has {len(prods)} entries; use 2-6 (us + 1-5 competitors)")
    if len(set(pids)) != len(pids):
        E("product ids must be unique")
    us = [p for p in prods if p.get("us")]
    if len(us) != 1:
        E("exactly one product needs us: true")
    for i, p in enumerate(prods):
        if not p.get("name") or not p.get("url"):
            E(f"products[{i}] needs name and url")
    us_id = us[0]["id"] if len(us) == 1 else None
    pset = set(pids)

    # matrix
    crits = a.get("criteria") or []
    cids = set()
    if len(crits) < 6:
        E(f"criteria has {len(crits)} rows; a teardown needs at least 6")
    lenses_seen = set()
    for i, c in enumerate(crits):
        p = f"criteria[{i}] '{c.get('id')}'"
        if not c.get("id") or not c.get("k"):
            E(f"criteria[{i}] needs id and k")
        if c.get("id") in cids:
            E(f"{p}: id used twice")
        cids.add(c.get("id"))
        if c.get("lens") not in LENSES:
            E(f"{p}.lens '{c.get('lens')}' is not one of {', '.join(sorted(LENSES))}")
        lenses_seen.add(c.get("lens"))
        cells = c.get("cells") or {}
        for pid in pids:
            cell = cells.get(pid)
            if cell is None:
                E(f"{p} has no cell for '{pid}': use v: \"nd\" (no data) instead of leaving it out")
                continue
            v = cell.get("v")
            if v not in VALUES:
                E(f"{p}.cells.{pid}.v must be yes, part, no or nd")
            if v != "nd":
                if not str(cell.get("t", "")).strip():
                    E(f"{p}.cells.{pid} needs t: what was seen")
                s = usable(cell.get("s"), f"{p}.cells.{pid}")
                claim_ok(s, pid, cell.get("claim"), f"{p}.cells.{pid}")
        for k in cells:
            if k not in pset:
                E(f"{p}.cells has '{k}', which is not a product id")
    missing = LENSES - lenses_seen
    if missing:
        W(f"no criteria for lens(es) {', '.join(sorted(missing))}: say in text.dataP why they were left out")
    nd = sum(1 for c in crits for x in (c.get("cells") or {}).values() if x.get("v") == "nd")
    total = sum(len(c.get("cells") or {}) for c in crits)
    if total and nd / total > .4:
        W(f"{nd} of {total} cells are 'no data': confidence should be low and say so")

    # canvas
    fac = (a.get("canvas") or {}).get("factors") or []
    if not 4 <= len(fac) <= 10:
        E(f"canvas has {len(fac)} factors; use 4-10")
    for i, f in enumerate(fac):
        p = f"canvas.factors[{i}] '{f.get('k')}'"
        lv = f.get("levels") or {}
        for pid in pids:
            x = lv.get(pid)
            if not isinstance(x, (int, float)) or not 0 <= x <= 10:
                E(f"{p}.levels.{pid} must be a number 0-10")
        b = f.get("basis") or []
        if not b:
            E(f"{p}.basis is empty: name the criteria the levels come from")
        for cid in b:
            if cid not in cids:
                E(f"{p}.basis '{cid}' is not a criterion id")

    # map
    mp = a.get("map") or {}
    for ax in ("x", "y"):
        if not all((mp.get(ax) or {}).get(k) for k in ("k", "lo", "hi")):
            E(f"map.{ax} needs k, lo and hi")
    for pid in pids:
        pt = (mp.get("points") or {}).get(pid)
        if not pt or not all(isinstance(pt.get(k), (int, float)) and 0 <= pt[k] <= 10 for k in ("x", "y")):
            E(f"map.points.{pid} needs x and y, 0-10")

    # errc
    errc = a.get("errc") or {}
    for k in ("eliminate", "reduce", "raise", "create"):
        if k not in errc:
            E(f"errc.{k} is missing (use [] if nothing)")
        for j, it in enumerate(errc.get(k) or []):
            if not it.get("t") or not it.get("why"):
                E(f"errc.{k}[{j}] needs t and why")
    if not any(errc.get(k) for k in ("raise", "create")):
        W("errc has nothing to raise or create: the teardown found no way to differ")

    # win / lose
    for side in ("win", "lose"):
        items = a.get(side) or []
        if not items:
            W(f"'{side}' is empty: " + ("a teardown that finds no losses is suspect" if side == "lose" else "say what we do better, or why nothing"))
        for j, it in enumerate(items):
            if not it.get("t") or not it.get("d"):
                E(f"{side}[{j}] needs t and d")
            if not it.get("s"):
                E(f"{side}[{j}] needs s: the sources behind it")
            for sid in it.get("s") or []:
                usable(sid, f"{side}[{j}]")
            for pid in it.get("vs") or []:
                if pid not in pset:
                    E(f"{side}[{j}].vs '{pid}' is not a product id")

    # moves
    ops = a.get("ops") or []
    detail, plans = a.get("detail") or {}, a.get("plans") or {}
    if not ops:
        E("ops is empty: a teardown ends in moves")
    pts = {}
    for i, o in enumerate(ops):
        oid = i + 1
        p = f"ops[{i}] (#{oid})"
        for k in ("I", "C", "E"):
            v = o.get(k)
            if not isinstance(v, int) or not 1 <= v <= 10:
                E(f"{p}.{k} must be a whole number 1-10")
        if o.get("x") not in ("opt", "ex"):
            E(f"{p}.x must be opt or ex")
        if o.get("ev") not in ("obs", "hyp"):
            E(f"{p}.ev must be obs or hyp")
        if o.get("a") not in AREAS:
            E(f"{p}.a '{o.get('a')}' must be one of {', '.join(sorted(AREAS))}")
        if not o.get("t"):
            E(f"{p}.t is missing")
        for pid in o.get("vs") or []:
            if pid not in pset or pid == us_id:
                E(f"{p}.vs '{pid}' is not a competitor id")
        if isinstance(o.get("I"), int) and isinstance(o.get("E"), int):
            pts.setdefault((o["E"], o["I"]), []).append(oid)
        d = detail.get(str(oid))
        if not d:
            E(f"{p} has no detail[\"{oid}\"]")
            continue
        if not str(d.get("why", "")).strip():
            E(f"detail[\"{oid}\"].why is empty")
        ev = d.get("evidence") or []
        if not ev:
            E(f"detail[\"{oid}\"].evidence is empty: every move needs the competitor evidence behind it")
        for j, e in enumerate(ev):
            w = f"detail[\"{oid}\"].evidence[{j}]"
            if e.get("p") not in pset:
                E(f"{w}.p '{e.get('p')}' is not a product id")
            if not e.get("t"):
                E(f"{w}.t is missing")
            s = usable(e.get("s"), w)
            claim_ok(s, e.get("p"), e.get("claim"), w)
        if len(d.get("steps") or []) < 2:
            E(f"detail[\"{oid}\"].steps needs at least 2 concrete steps")
        for k in ("metric", "effort", "risk"):
            if not str(d.get(k, "")).strip():
                E(f"detail[\"{oid}\"].{k} is missing")
        if o.get("ev") == "hyp" and isinstance(o.get("C"), int) and o["C"] > 7:
            W(f"{p} is a hypothesis with confidence {o['C']}: above 7 needs evidence")
    for pt, ids in pts.items():
        if len(ids) > 2:
            W(f"moves {ids} share one matrix point; check the scores")
    for k in detail:
        if not k.isdigit() or not 1 <= int(k) <= len(ops):
            E(f"detail[\"{k}\"] does not match any move")
    ranked = sorted(range(1, len(ops) + 1), key=lambda j: (-(ops[j - 1].get("I", 0) * ops[j - 1].get("C", 0) * ops[j - 1].get("E", 0)), j))
    for oid in ranked[:3]:
        pl = plans.get(str(oid))
        if not pl or not all(str(pl.get(k, "")).strip() for k in ("h", "m", "t")):
            E(f"top-3 move #{oid} needs plans[\"{oid}\"] with h, m, t")
        d = detail.get(str(oid)) or {}
        for k in ("alt", "rtype", "thr", "pm"):
            if not d.get(k):
                E(f"top-3 move #{oid} needs detail.{k} (alternatives, risk type, threshold, pre-mortem)")
    for k, it in ((k, it) for k in ("eliminate", "reduce", "raise", "create") for it in errc.get(k) or []):
        if it.get("op") and not 1 <= it["op"] <= len(ops):
            E(f"errc.{k} item '{it.get('t')}' points to move #{it['op']}, which does not exist")

    # KPIs
    for i, k in enumerate(a.get("kpis") or []):
        v = str(k.get("v", ""))
        if not TOKENS.search(v) and re.search(r"\d", v):
            sid = k.get("src")
            if not sid:
                E(f"kpis[{i}] '{v}' has a number but no src")
            elif sid not in src:
                E(f"kpis[{i}].src '{sid}' is not a source id")
            elif src[sid].get("status") == "no":
                E(f"kpis[{i}] cites '{sid}', which is marked as not available")

    for i, q in enumerate(a.get("answers") or []):
        if not q.get("q") or not q.get("a"):
            E(f"answers[{i}] needs q and a (for a skipped question, a = the assumption taken)")
    gl = a.get("glossary") or {}
    for k, v in gl.items():
        if not v.get("g") or not v.get("d"):
            E(f"glossary['{k}'] needs g and d")
    if not gl:
        W("glossary is empty: terms will have no tooltips")

    # quotes
    for path, s in strings({k: v for k, v in a.items() if k not in ("glossary",)}):
        for m in QUOTES.finditer(s):
            q = next(g for g in m.groups() if g)
            n = len(q.split())
            if n > MAX_QUOTE:
                E(f"{path}: quote of {n} words (max {MAX_QUOTE}); paraphrase instead: \"{q[:60]}...\"")
    return err, warn


def main():
    args = sys.argv[1:]
    today = None
    if "--today" in args:
        i = args.index("--today")
        today = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__)
        return 2
    with open(args[0], encoding="utf-8") as f:
        try:
            a = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] not valid JSON: {e}")
            return 1
    err, warn = validate(a, today)
    for e in err:
        print("[ERROR]", e)
    for w in warn:
        print("[WARN] ", w)
    print("OK" if not err else f"{len(err)} error(s)")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
