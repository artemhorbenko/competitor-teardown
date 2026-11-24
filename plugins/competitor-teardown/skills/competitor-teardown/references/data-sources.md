# Data sources

Check what this session can reach before gathering (ToolSearch or the tool list). Never assume a connector exists, never fill a gap with invented numbers, and use every source read-only. Public pages and review sites are enough for a useful teardown; private data (CRM, analytics) sharpens the moves.

## Status and kind

| Status | When |
|---|---|
| `ok` | Opened and used, or the requester's own answer. |
| `demo` | Partial: a free tier, a third-party summary of a page you could not open, a search snippet instead of the page, a screenshot with a cut-off range. |
| `no` | Not connected, blocked, or erroring after one retry. Cells may not cite it. |

`kind` says who is speaking, which decides how a fact may be used:

| kind | Meaning | Use |
|---|---|---|
| `own` | A vendor about itself (`by` = that product) | Fact about that vendor's offer as stated by them. |
| `rival` | A vendor about a competitor (`by` = the publisher) | About the subject it is a **claim**: cite with `claim: true`, and check it against the subject's own pages. |
| `review` | Review sites, app stores | Ratings, counts, themes; always with the date. |
| `third` | Press, analysts, databases (Tranco, Crunchbase, Wayback) | Facts with their date; third-party comparisons of prices are usually `demo`. |
| `data` | Analytics, CRM, call notes | Only from the requester. |
| `owner` | The requester's answers | Context and assumptions. |
| `tool` | A connector (Similarweb, Ahrefs) | Numbers with period and definition. |

Confidence in the report is the average of ok = 1, demo = 0.6, no = 0, so list only sources that matter.

## Where each fact lives

### Vendor sites (all products, ours included)
- **Tools:** Claude in Chrome or another browser for pages that need scripts; WebFetch for static pages.
- **Pages:** homepage, pricing, product/platform, integrations, developers/docs/API, customers/case studies, industries, comparison/alternatives, careers, changelog, legal (for contract length).
- **Find hidden pages:** `/sitemap.xml`, site search, the footer, web search `site:<domain> <our name>`.
- **Don't:** sign up, start a trial, request a demo, fill a form, chat with a bot, or email anyone.

### Comparison pages aimed at us
- Web search: `<competitor> vs <us>`, `<us> alternatives`, `switch from <us>`, `migrate from <us>`.
- Record every claim they make about us with `claim: true` and check it against our own pages; a contradiction is a finding (and a move).
- Note the page's "last updated" date if shown.

### Reviews
- **G2, Capterra, Software Advice, Trustpilot, Shopify App Store, Apple App Store, Google Play.** Many review pages block fetch tools; try the browser, then web search snippets (mark `demo`).
- Record per site: rating, review count, the listing URL, the date, 2-3 recurring themes in your words. G2's category comparison pages also show "ease of setup" and "time to implement" scores.
- Do not mix sites in one number. Do not quote reviewers beyond 15 words.

### Light SEO footprint
- **Tranco** (tranco-list.eu): the domain's rank in the top-1M list; say which list date. Not a traffic number.
- Sitemap size and blog/resource categories show topic ownership; a benchmark report or hub is a strong signal.
- With Ahrefs or Semrush connected: Domain Rating, organic keywords count, top pages. Without a paid plan most tools fail on other domains; mark them `no`.

### Hiring and funding
- Careers page (count of open roles, teams, locations), Crunchbase public profile (last round, date), press releases. Crunchbase often blocks fetch; use web search snippets as `demo`.

### Changes over time
- **Wayback Machine:** `https://web.archive.org/web/<YYYYMMDD>/<url>` for the homepage and pricing page about 12 months ago (and 6 months if useful). Compare headline, price, plans, new pages. Cite the snapshot URL with its own date in the note.

### Private data (only from the requester)
- CRM win/loss reasons, call recordings, sales notes ("deals lost to X because..."), traffic analytics. Ask in step 1; one sentence about lost deals is often the strongest evidence in the report.

## Recording

For every fact keep: URL, checked-on date (YYYY-MM-DD), who published it (`kind`, `by`), what you saw in your words, and for numbers the definition and period. A KPI with a number must name its source id.
