# Results

Scores 1-5: **S** sourcing (every cell traces to a dated URL that says it), **F** fairness (same criteria and depth for every product; claims marked as claims), **M** moves specific and tied to competitor evidence, **R** report renders on desktop, tablet and phone, **H** hands-off file usable by an agent without the report.

| Date | Version | Scenario | Setup | S | F | M | R | H | Time | What broke |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-24 | 1.0.0 | public-only-b2b, rival-claims | B2B SaaS (referral platform) vs 4 competitors; browser + web search; no CRM or traffic; 4 of 4 questions answered | 4 | 5 | 4 | 5 | 4 | ~2.5 h incl. fact check | Independent fact check corrected 15 of 101 cells: a fetch tool's page summary had added a figure not on the page (caught before use), "none found" missed comparison pages linked in a footer, one Tranco URL was cited for all domains, a funding claim was stronger than its source. Led to rules: read page text, footer before "no", one source per URL. Our product's own comparison pages had been removed since a run 3 days earlier. Fact check stalled twice on browser permission prompts. |
