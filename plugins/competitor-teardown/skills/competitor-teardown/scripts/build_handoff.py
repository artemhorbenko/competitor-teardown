#!/usr/bin/env python3
"""Turn a competitor-teardown audit.json into a hands-off file for an AI agent or a developer.

Usage: python build_handoff.py audit.json handoff.md [--json tasks.json]

The report page is for people; this file is for whoever implements the moves.
Plain Markdown, no design: context, products, where we win and lose, ERRC,
sources, rules, then one task per move in priority order with the competitor
evidence behind it (with URL and checked-on date), steps, acceptance criteria
and a way to verify. Optional tasks.json carries the same tasks for a tracker.
Standard library only.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate_audit import validate  # noqa: E402

TOKENS = re.compile(r"\{(lead|trail|crit|cells|qw|n|conf)\}")
L = {
    "en": dict(title="Hands-off", intro="Implementation brief generated from a competitor teardown. Work top to bottom: tasks are ordered by ICE, and a task always comes after the ones it depends on. Each task lists the competitor evidence behind it; re-check a source if its date is more than 30 days old. Treat \"hypothesis\" tasks as experiments: test before building fully.",
               context="Context", finding="Main finding", products="Products compared", us="us", win="Where we win", lose="Where we lose",
               errc="ERRC", errc_k={"eliminate": "Eliminate", "reduce": "Reduce", "raise": "Raise", "create": "Create"},
               answers="Requester answers and assumptions", skipped="skipped", sources="Sources", checked="checked", missing="Missing, so lower confidence",
               rules="Rules for the implementer", tasks="Tasks", order="Suggested order", type_o="optimize", type_x="explore", ev_o="observed", ev_h="hypothesis",
               area="Area", vs="Answers", against="vs", ice="ICE", type="Type", evidence="Evidence", why="Why", comp="Competitor evidence", claim="claim by",
               steps="Steps", accept="Acceptance criteria", verify="How to verify", metric="Metric", effort="Effort", risk="Risk / guardrail",
               alt="Alternatives rejected", pm="Pre-mortem", hypo="Hypothesis", copy="Copy variants", top="top 3", dep="Depends on", task="Task",
               conf="Confidence", glossary="Glossary", trail="Criteria where we trail the best competitor", lead_="Criteria where we lead outright",
               areas=dict(page="page", message="message", pricing="pricing", feature="feature", content="content", proof="proof", sales="sales", data="data"),
               default_rules=["Do not invent numbers, customers, logos, reviews or quotes. If a claim cannot be sourced, leave it out.",
                              "Anything you publish about a competitor must cite a public URL and the date it was checked; re-check it the day you publish.",
                              "Do not copy competitor text. Quote at most 15 words, in quotation marks, with the source; otherwise paraphrase.",
                              "One vendor's statement about another is a claim, not a fact: never repeat it as fact.",
                              "Do not change public prices, plans or legal terms without the owner's written approval.",
                              "Do not submit real forms, sign up for trials or contact competitors' sales teams while testing.",
                              "When a task is a hypothesis, run the cheapest test first and stop if the threshold is not met."]),
    "uk": dict(title="Hands-off", intro="Бриф на впровадження, згенерований з розбору конкурентів. Ідіть згори донизу: задачі впорядковано за ICE, і кожна стоїть після тих, від яких залежить. Біля кожної задачі — докази з боку конкурентів; перевірте джерело заново, якщо його даті понад 30 днів. Задачі з позначкою «гіпотеза» — це експерименти: спершу перевірка, потім повна реалізація.",
               context="Контекст", finding="Головна знахідка", products="Продукти в порівнянні", us="ми", win="Де ми виграємо", lose="Де ми програємо",
               errc="ERRC", errc_k={"eliminate": "Прибрати", "reduce": "Зменшити", "raise": "Підсилити", "create": "Створити"},
               answers="Відповіді замовника й припущення", skipped="пропущено", sources="Джерела", checked="перевірено", missing="Бракує, тому впевненість нижча",
               rules="Правила для виконавця", tasks="Задачі", order="Рекомендований порядок", type_o="оптимізація", type_x="дослідження", ev_o="спостережено", ev_h="гіпотеза",
               area="Сфера", vs="Проти кого", against="проти", ice="ICE", type="Тип", evidence="Доказ", why="Чому", comp="Докази з боку конкурентів", claim="твердження від",
               steps="Кроки", accept="Критерії приймання", verify="Як перевірити", metric="Метрика", effort="Зусилля", risk="Ризик / запобіжник",
               alt="Відкинуті альтернативи", pm="Pre-mortem", hypo="Гіпотеза", copy="Варіанти тексту", top="топ-3", dep="Залежить від", task="Задача",
               conf="Впевненість", glossary="Глосарій", trail="Критеріїв, де ми поступаємося найкращому конкуренту", lead_="Критеріїв, де ми попереду",
               areas=dict(page="сторінка", message="меседж", pricing="ціни", feature="функція", content="контент", proof="докази", sales="продажі", data="дані"),
               default_rules=["Не вигадувати цифр, клієнтів, логотипів, відгуків чи цитат. Якщо твердження не можна підкріпити джерелом — не писати його.",
                              "Усе, що публікуємо про конкурента, має посилатися на публічний URL і дату перевірки; перевірити заново в день публікації.",
                              "Не копіювати тексти конкурентів. Цитата — до 15 слів, у лапках, з джерелом; інакше переказ своїми словами.",
                              "Слова одного вендора про іншого — це твердження, а не факт: не подавати їх як факт.",
                              "Не змінювати публічні ціни, плани чи юридичні умови без письмового погодження власника.",
                              "Під час тестів не відправляти справжні форми, не реєструвати тріали й не писати відділам продажів конкурентів.",
                              "Якщо задача — гіпотеза, спершу найдешевший тест; зупинитися, якщо поріг не досягнуто."]),
}
SCORE = {"yes": 2, "part": 1, "no": 0}


def counts(a):
    prods = a.get("products") or []
    us = next((p["id"] for p in prods if p.get("us")), None)
    comp = [p["id"] for p in prods if p["id"] != us]
    lead = trail = cells = 0
    for c in a.get("criteria") or []:
        cs = c.get("cells") or {}
        cells += sum(1 for x in cs.values() if x.get("v") != "nd")
        ours = SCORE.get((cs.get(us) or {}).get("v"))
        th = [SCORE[(cs.get(p) or {}).get("v")] for p in comp if (cs.get(p) or {}).get("v") in SCORE]
        if ours is not None and th:
            lead += ours > max(th)
            trail += ours < max(th)
    return lead, trail, cells


def clean(s, ctx):
    s = TOKENS.sub(lambda m: str(ctx.get(m.group(1), m.group(0))), str(s))
    return s.replace("[[", "**").replace("]]", "**")


def build(a):
    lang = (a.get("lang") or "en")[:2]
    t = L.get(lang, L["en"])
    ops = a.get("ops") or []
    detail, plans = a.get("detail") or {}, a.get("plans") or {}
    sources = a.get("sources") or []
    src = {s.get("id"): s for s in sources}
    prods = a.get("products") or []
    pn = {p["id"]: p.get("name", p["id"]) for p in prods}
    conf = round(sum({"ok": 1, "demo": .6}.get(s.get("status"), 0) for s in sources) / len(sources) * 100) if sources else 0
    qw = sum(1 for o in ops if o.get("I", 0) >= 6 and 11 - o.get("E", 0) <= 5)
    lead, trail, cells = counts(a)
    ctx = dict(lead=lead, trail=trail, crit=len(a.get("criteria") or []), cells=cells, qw=qw, n=len(ops), conf=conf)
    text = a.get("text") or {}

    def cite(sid):
        s = src.get(sid) or {}
        bits = [s.get("name", sid)]
        if s.get("url"):
            bits.append(s["url"])
        if s.get("date"):
            bits.append(f"{t['checked']} {s['date']}")
        return " · ".join(bits)

    def ev_line(e):
        s = src.get(e.get("s")) or {}
        cl = f" _({t['claim']} {pn.get(s.get('by'), s.get('by'))})_" if e.get("claim") else ""
        return f"**{pn.get(e.get('p'), e.get('p'))}:** {e.get('t')}{cl} — {cite(e.get('s'))}"

    tasks = []
    for i, o in enumerate(ops, 1):
        d = detail.get(str(i), {})
        p = plans.get(str(i), {})
        accept = list(d.get("accept") or [])
        if not accept:
            if d.get("thr"):
                accept.append(d["thr"])
            if d.get("metric"):
                accept.append(f"{t['metric']}: {d['metric']}")
        tasks.append(dict(
            id=f"T{i:02d}", n=i, title=o.get("t"), area=o.get("a"), against=[pn.get(v, v) for v in o.get("vs") or []],
            type="explore" if o.get("x") == "ex" else "optimize",
            evidence_type="hypothesis" if o.get("ev") == "hyp" else "observed",
            impact=o.get("I"), confidence=o.get("C"), ease=o.get("E"),
            ice=o.get("I", 0) * o.get("C", 0) * o.get("E", 0),
            why=d.get("why", ""),
            competitor_evidence=[dict(product=pn.get(e.get("p"), e.get("p")), seen=e.get("t"), claim=bool(e.get("claim")),
                                      source=(src.get(e.get("s")) or {}).get("name"), url=(src.get(e.get("s")) or {}).get("url"),
                                      checked=(src.get(e.get("s")) or {}).get("date")) for e in d.get("evidence") or []],
            _ev_lines=[ev_line(e) for e in d.get("evidence") or []],
            steps=d.get("steps") or [], acceptance=accept,
            verify=p.get("t") or (d.get("verify") or ""), hypothesis=p.get("h", ""),
            metric=d.get("metric", ""), effort=d.get("effort", ""), risk=d.get("risk", ""),
            alternatives=d.get("alt") or [], risk_type=d.get("rtype", ""), pre_mortem=d.get("pm", ""),
            copy=d.get("copy") or [], depends_on=d.get("depends") or [],
        ))
    tasks.sort(key=lambda x: (-x["ice"], x["n"]))
    by_id, done, ordered = {tk["id"]: tk for tk in tasks}, set(), []

    def place(tk, seen=()):
        if tk["id"] in done or tk["id"] in seen:
            return
        for dep in tk["depends_on"]:
            if dep in by_id:
                place(by_id[dep], seen + (tk["id"],))
        done.add(tk["id"])
        ordered.append(tk)
    for tk in tasks:
        place(tk)
    tasks = ordered
    for rank, tk in enumerate(tasks, 1):
        tk["rank"] = rank

    out = []
    w = out.append
    w(f"# {t['title']}: {a.get('title', '')}".rstrip(": "))
    w("")
    w(t["intro"])
    w("")
    w(f"## {t['context']}")
    w("")
    if text.get("headline"):
        w(f"- **{t['finding']}:** {clean(text['headline'], ctx).replace('**', '')}")
    if text.get("lead"):
        w(f"- {clean(text['lead'], ctx)}")
    w(f"- **{t['trail']}:** {trail} / {ctx['crit']} · **{t['lead_']}:** {lead}")
    w(f"- **{t['conf']}:** {conf}%")
    w("")
    w(f"### {t['products']}")
    w("")
    for p in prods:
        mark = f" ({t['us']})" if p.get("us") else ""
        w(f"- **{p.get('name')}**{mark} — {p.get('url')}" + (f" — {p['tag']}" if p.get("tag") else ""))
    w("")
    for side, head in (("win", t["win"]), ("lose", t["lose"])):
        items = a.get(side) or []
        if items:
            w(f"### {head}")
            w("")
            for it in items:
                vs = f" ({t['against']} {', '.join(pn.get(v, v) for v in it['vs'])})" if it.get("vs") else ""
                w(f"- **{it.get('t')}**{vs}. {it.get('d')} Sources: " + "; ".join(cite(s) for s in it.get("s") or []))
            w("")
    errc = a.get("errc") or {}
    if any(errc.get(k) for k in t["errc_k"]):
        w(f"### {t['errc']}")
        w("")
        for k, lab in t["errc_k"].items():
            for it in errc.get(k) or []:
                op = f" → T{it['op']:02d}" if it.get("op") else ""
                w(f"- **{lab}:** {it.get('t')}{op}. {it.get('why')}")
        w("")
    if a.get("answers"):
        w(f"### {t['answers']}")
        w("")
        for q in a["answers"]:
            mark = f" ({t['skipped']})" if q.get("skipped") else ""
            w(f"- {q.get('q')}{mark}: {q.get('a')}")
        w("")
    if sources:
        w(f"### {t['sources']}")
        w("")
        for i, s in enumerate(sources, 1):
            extra = " · ".join(x for x in (s.get("url"), f"{t['checked']} {s['date']}" if s.get("date") else "", s.get("note")) if x)
            w(f"{i}. [{s.get('status')}] {s.get('name')}" + (f" — {extra}" if extra else ""))
        miss = [s.get("name") for s in sources if s.get("status") == "no"]
        if miss:
            w("")
            w(f"{t['missing']}: {', '.join(miss)}.")
        w("")
    w(f"## {t['rules']}")
    w("")
    for r in (a.get("rules") or t["default_rules"]):
        w(f"- {r}")
    w("")
    w(f"## {t['order']}")
    w("")
    w(f"| # | ID | {t['task']} | {t['area']} | {t['vs']} | {t['ice']} | {t['type']} | {t['evidence']} |")
    w("|---|---|---|---|---|---|---|---|")
    for tk in tasks:
        top = f" ({t['top']})" if tk["rank"] <= 3 else ""
        w(f"| {tk['rank']} | {tk['id']} | {tk['title']}{top} | {t['areas'].get(tk['area'], tk['area'])} | {', '.join(tk['against']) or '—'} | {tk['ice']} | {t['type_x'] if tk['type'] == 'explore' else t['type_o']} | {t['ev_h'] if tk['evidence_type'] == 'hypothesis' else t['ev_o']} |")
    w("")
    w(f"## {t['tasks']}")
    for tk in tasks:
        w("")
        w(f"### {tk['rank']}. {tk['id']} — {tk['title']}")
        w("")
        w(f"- {t['area']}: {t['areas'].get(tk['area'], tk['area'])} · {t['vs']}: {', '.join(tk['against']) or '—'} · {t['ice']} {tk['ice']} = {tk['impact']}×{tk['confidence']}×{tk['ease']} · {t['type']}: {t['type_x'] if tk['type'] == 'explore' else t['type_o']} · {t['ev_h'] if tk['evidence_type'] == 'hypothesis' else t['ev_o']}")
        if tk["effort"]:
            w(f"- {t['effort']}: {tk['effort']}")
        if tk["depends_on"]:
            w(f"- {t['dep']}: {', '.join(tk['depends_on'])}")
        w("")
        if tk["why"]:
            w(f"**{t['why']}.** {tk['why']}")
            w("")
        if tk["_ev_lines"]:
            w(f"**{t['comp']}:**")
            w("")
            for x in tk["_ev_lines"]:
                w(f"- {x}")
            w("")
        if tk["hypothesis"]:
            w(f"**{t['hypo']}.** {tk['hypothesis']}")
            w("")
        if tk["steps"]:
            w(f"**{t['steps']}:**")
            w("")
            for j, s in enumerate(tk["steps"], 1):
                w(f"{j}. {s}")
            w("")
        if tk["acceptance"]:
            w(f"**{t['accept']}:**")
            w("")
            for c in tk["acceptance"]:
                w(f"- [ ] {c}")
            w("")
        if tk["verify"]:
            w(f"**{t['verify']}:** {tk['verify']}")
            w("")
        if tk["risk"]:
            w(f"**{t['risk']}:** {tk['risk']}")
            w("")
        if tk["alternatives"]:
            w(f"**{t['alt']}:**")
            w("")
            for x in tk["alternatives"]:
                w(f"- {x}")
            w("")
        if tk["pre_mortem"]:
            w(f"**{t['pm']}:** {tk['pre_mortem']}")
            w("")
        if tk["copy"]:
            w(f"**{t['copy']}:**")
            w("")
            for x in tk["copy"]:
                w(f"- {x}")
            w("")
    gl = a.get("glossary") or {}
    if gl:
        w(f"## {t['glossary']}")
        w("")
        for k, v in gl.items():
            w(f"- **{k}** ({v.get('g')}): {v.get('d')}")
        w("")
    for tk in tasks:
        tk.pop("_ev_lines", None)
    return "\n".join(out).rstrip() + "\n", tasks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audit")
    ap.add_argument("out")
    ap.add_argument("--json", help="also write tasks as JSON for a tracker")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    with open(a.audit, encoding="utf-8") as f:
        audit = json.load(f)
    err, _ = validate(audit)
    if err and not a.force:
        for e in err:
            print("[ERROR]", e)
        print("Not built. Fix audit.json or pass --force.")
        return 1
    md, tasks = build(audit)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(md)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump({"title": audit.get("title"), "lang": audit.get("lang"), "products": audit.get("products"), "tasks": tasks}, f, ensure_ascii=False, indent=1)
    print(f"Written {a.out} ({len(tasks)} tasks)" + (f" and {a.json}" if a.json else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
