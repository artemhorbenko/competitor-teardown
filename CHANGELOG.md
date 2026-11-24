# Changelog

## 1.0.0 - 2026-11-24

First public release.

- 12 teardown lenses, the same for every product: positioning, buyer, breadth, pricing, proof, comparison pages aimed at us, onboarding, integrations (API, MCP), reviews, light SEO footprint, hiring and funding, changes over time.
- Process: source check (ok / demo / no), up to 4 skippable questions (our product, competitors, buyer, decision), gathering, findings labelled observed or hypothesis, ICE, top 3 with alternatives, threshold and pre-mortem, validation, both outputs, render check, fact check of every cell.
- One `audit.json`, two outputs: the report page (`build_report.py`) and the hands-off file for AI agents (`build_handoff.py` → `handoff.md` + `tasks.json`).
- Report template in the product-lens-audit design: comparison matrix with a numbered, dated source per cell and filters (all / differences / where we trail), Blue Ocean strategy canvas, ERRC grid, positioning map, where we win / lose, impact-effort matrix, moves table, next 3, full plan, sources with kind and date. uk/en labels, tooltips for every term, stacked tables on phones, dark theme.
- `validate_audit.py`: a dated source on every cell, one vendor's claim about another marked as a claim, quotes up to 15 words, competitor evidence on every move, top-3 rules, KPI sources.
- `check_report.py`: desktop, tablet, phone; canvas lines, chart labels overlapping or cut off, dead source links, phone table cells, tooltips, filters.
- Rules learned from the first test runs: audit only each product's production domain; read page text, not fetch-tool summaries; check the footer before "none found"; one source per URL; read every product's case-studies page.
- English demo with fictional companies and its hands-off file.
