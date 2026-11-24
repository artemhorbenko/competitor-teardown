---
name: competitor-teardown
description: Tear down a product's competitors from public pages and review sites - positioning, buyer, product breadth, pricing, proof, comparison pages aimed at you, onboarding, integrations (API, MCP), reviews (G2, Capterra, app stores), SEO footprint, hiring and funding, changes over time - and deliver a sourced comparison matrix, strategy canvas, ERRC grid, positioning map and prioritized moves, as a visual report for people and a hands-off brief for AI agents. Use when someone asks to compare their product with competitors, do a competitive analysis or teardown, find where they win or lose against rivals, or answer a competitor's comparison page.
---

# Competitor Teardown

Compare one product ("us") with 1-5 competitors through the same 12 lenses, cite a public source with a checked-on date for every cell, and turn the gaps into a short list of concrete moves. One `audit.json` feeds two outputs: a report page for people and a hands-off brief for whoever implements the moves, often another AI agent.

Respond in the user's language, and write the report in it too.

Files next to this SKILL.md (read each when its step comes, not up front):
- `references/lenses.md` - the 12 teardown lenses, what to look for, which pages answer each, how to turn them into criteria (steps 2-3).
- `references/data-sources.md` - which tools to look for, where each public fact lives, fallbacks, what to mark `no` (steps 0 and 2).
- `references/report-spec.md` and `references/audit.schema.json` - the report's sections and the data shape (step 6).
- `assets/report-template.html` - the report page; it renders everything from one JSON block. `assets/example-teardown.en.json` is a full example (fictional companies), `assets/example-handoff.en.md` the matching hands-off file.
- `scripts/validate_audit.py`, `scripts/build_report.py`, `scripts/build_handoff.py`, `scripts/check_report.py` - data check, page build, hands-off build, render check (steps 6-7).

## 0. Check which sources are connected

Look at the tools this session actually has (search the tool list / ToolSearch; never assume): a browser, web search and fetch, and any connector for traffic (Similarweb, Ahrefs, Semrush), company data (Crunchbase), CRM or call notes. Give each a status: `ok` (used), `demo` (partial: a free tier, a third-party summary, a screenshot with a cut-off range), `no` (not connected, or erroring after one retry). Say in one line which important source is missing and continue; never fill the gap with invented numbers.

## 1. Ask the requester (every question skippable)

First look for saved context: a previous `audit.json` from this skill or from product-lens-audit, or a `competitor-teardown-context.md`. With a previous teardown, say what changed since then for each competitor (use its dates).

Then ask one round of up to 4 questions, each with a "Skip" option (AskUserQuestion or similar; otherwise plain text). Never block: if skipped, state the assumption and continue.
- **Our product**: name and URL, and which product line if there are several.
- **Competitors**: up to 5. If skipped, pick them from comparison pages, "alternatives" lists and review-site categories, and say how you picked.
- **The buyer**: who signs and who uses (for B2B: role, company size, industry).
- **What decision this informs**: website and messaging, pricing, roadmap, sales battlecards, or a board update. It decides which moves matter.

Record each answer in `answers` (a skipped one shows the assumption) and add an `owner` source.

## 2. Gather, the same way for every product

Read `references/lenses.md` and `references/data-sources.md`. Walk the same pages for every product, including ours: homepage, pricing, product and integrations pages, docs or developer pages, customers or case studies, comparison and "alternatives" pages, careers. Then review sites (G2, Capterra, Software Advice, app stores), a Tranco rank, Crunchbase or press for funding, and Wayback Machine snapshots from about 12 months ago.

For every fact keep: the URL, the date you checked it, what you saw in your own words, and who published it. Rules while gathering:
- Public pages and review sites only. No sign-ups, trials, demo requests, forms or contacting anyone at a competitor.
- **Quote at most 15 words**, in quotation marks, and only when the exact words matter (a headline, a claim aimed at us). Otherwise paraphrase.
- **One vendor's words about another are a claim, not a fact.** When a competitor's comparison page says something about us (or about a third vendor), record it with `claim: true` and check it against the subject's own pages; a contradiction is itself a finding.
- A missing page is a finding only after you looked for it (the footer first, then the sitemap and a `site:` search). Otherwise mark the cell `nd` (no data).
- **Read the page itself.** A fetch tool that returns a model's summary of a page can add facts that are not on it; use it to find pages, then confirm each fact in the page text (browser or raw HTML) before it goes into a cell.
- One source = one URL. When the same tool answers for several products (Tranco, an app-store search, a G2 page), add one source per product's URL.
- A rival page you used before may be gone: re-open every URL on the day of the run; a 404 on our own comparison page is itself a finding.
- Review ratings and counts change daily: record them with the date, and say which listing.

## 3. Build the matrix

Turn the lenses into 12-24 criteria phrased so that every product can be judged the same way ("Price shown on the pricing page", not "Good pricing"). Fill every cell: `yes` (✓), `part` (◐), `no` (✗) or `nd` (no data, never guessed), a short note of what was seen, and the source id. Keep the scale consistent per row and say it in `matrixP` when it is not obvious (for ratings: what counts as ✓).

The template computes where we trail (our cell below the best competitor) and where we lead; those counts drive the headline.

## 4. Find the strategic picture

- **Strategy canvas** (Blue Ocean): 5-10 factors buyers compare, an offering level 0-10 per product, each factor tied to the matrix rows it is judged from (`basis`). Look for where the lines run together (no one wins) and where they split.
- **ERRC grid**: what we should eliminate, reduce, raise and create. Link items to moves (`op`).
- **Positioning map**: two axes that actually separate the products (for example self-serve ↔ managed, referrals only ↔ full suite), points 0-10, judged from the matrix.
- **Where we win / where we lose**: 2-5 points each, each with its sources and the competitors involved. A teardown that finds no losses is suspect; look again.

Label everything here a judgment from the matrix; it is not measured data.

## 5. Turn gaps into moves and prioritize

Write 6-12 moves. Each move is concrete: a page, a message, a pricing change, a feature, content, proof, a sales asset or data/tracking. Each has the competitor evidence behind it (product, what was seen, source), `vs` (which competitors it answers), and is labelled **observed** (the gap is visible on public pages) or **hypothesis** (the effect is unknown).

- Score Impact, Confidence, Ease 1-10; ICE = product. A hypothesis rarely deserves confidence above 7.
- Type: **Optimize** (fix what exists) or **Explore** (a different offer, segment or model). Mostly the first.
- For the top 3: at least 2 alternatives considered, the risk type (value, usability, viability, feasibility), a success threshold, a pre-mortem ("it is 3 months later and this failed - why?"), and the cheapest test.
- Copy changes get 2 alternative wordings with a one-line reason each.
- Missing data that blocks a decision (no traffic, no win/loss reasons) is its own move.
- Never recommend copying a competitor's text or design, disparaging them without a source, or any manipulative tactic.

## 6. Write audit.json and build both outputs

Read `references/report-spec.md`. Write one `audit.json` following `references/audit.schema.json` (start from `assets/example-teardown.en.json`). You write data only; the template draws every table, chart and label, and computes ICE, lead/trail counts, quick wins and confidence.

- **With a shell:**
  - `python scripts/build_report.py audit.json report.html` - runs `validate_audit.py` first and refuses to build on errors: a cell without a dated source, one vendor's claim about another not marked `claim`, a quote over 15 words, a move without competitor evidence, a top-3 move without alternatives or pre-mortem, a KPI number without a source. Fix the data, not the template.
  - `python scripts/build_handoff.py audit.json handoff.md --json tasks.json` - the hands-off brief: context, products, where we win and lose, ERRC, sources with dates, rules for the implementer, and every move as a task in ICE order (dependencies first) with competitor evidence, steps, acceptance criteria and how to verify. Add `accept`, `depends` and `verify` to `detail` and top-level `rules` when the defaults are not specific enough.
- **Without a shell** (Claude app without code execution): copy `assets/report-template.html`, set `<html lang>` and `<title>`, replace the content of `<script type="application/json" id="audit">` with your JSON (write `<\/` instead of `</` inside strings), check the `validate_audit.py` rules yourself, and write the hands-off file by hand in the structure of `assets/example-handoff.en.md`.

Interface labels come from the template's `UI` dictionary chosen by `<html lang>` (`uk`, `en`; add an entry with the same keys for another language). Save `audit.json` next to the report: the next run compares against it.

## 7. Render check

When Python and a Chromium-based browser are available (`pip install playwright`, `playwright install chromium`): `python scripts/check_report.py report.html --out ./report-check`. It opens the page at desktop (1280px), tablet (820px, touch) and phone (390px, touch) and fails on page errors, sideways scroll, empty charts, a canvas line missing, overlapping or cut-off chart labels, source links that point nowhere, table cells not wrapped in one `.cv`, tooltips that do not open on hover or tap or do not close on a second tap, and filters that break a table. Look at the screenshots (including dark mode), fix and re-check at most twice. Without a headless browser, open the published page with any browser tool at desktop and narrow width; if none exists, say which visual checks were not done.

## 8. Fact check every cell

Every matrix cell, KPI, win/lose point and evidence line must match its source on the date given. In Claude Code, give this to a separate subagent that has not seen your reasoning: pass it `audit.json` and ask it to open each source URL and list every cell it cannot confirm, every quote over 15 words, and every claim presented as fact. Elsewhere, do the pass yourself, source by source. Fix or downgrade (`nd`, `claim: true`, or `demo` source) what does not hold; never keep a cell because it supports the story. The checker opens many sites: in Claude in Chrome, allow each site once for the session so the check does not stall on permission prompts.

## 9. Deliver (only after steps 7 and 8 pass)

- The report: one self-contained HTML page. Publish it as an artifact when an artifact tool exists (private by default), otherwise send the .html file.
- The hands-off file (`handoff.md`, optional `tasks.json`): deliver next to the report as a file, and say in one line it is for an AI agent or developer.
- In chat: 3-5 summary bullets, the link or files, and one line on what was checked and what was missing.

## Rules
- Every cell, number and claim cites a public URL and a checked-on date, or is `nd`.
- Same criteria and the same depth for every product, ours included; do not grade ourselves on intentions.
- Quote competitors ≤15 words; otherwise paraphrase. Never reproduce their pages.
- Never present one vendor's claims about another as fact.
- No invented numbers, customers, logos, reviews, prices or roadmap guesses. "No data" is an answer.
- Public sources only; no sign-ups, demo requests, fake personas or contacting competitors.
- Prefer fewer, sharper moves; most should be optimizations of what exists.
