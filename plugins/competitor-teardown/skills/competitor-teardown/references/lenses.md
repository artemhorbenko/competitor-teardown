# The 12 teardown lenses

Apply every lens to every product, ours included, with the same depth. Each lens becomes 1-3 matrix criteria (`criteria[].lens` = the id below). A criterion is a question every product can answer the same way; write the answer for each product as `yes` / `part` / `no` / `nd` plus a short note and a source.

| id | Lens | Ask | Where to look | Example criteria |
|---|---|---|---|---|
| `pos` | Positioning and promise | What do they promise, to whom, in one line? Is it specific and checkable? | Homepage hero, title tag, meta description, About | One clear promise above the fold; Promise names an outcome with a number |
| `buyer` | Target buyer and industries | Who are they built for: size, role, industry, platform? | Pricing tiers, industry/solutions pages, case-study logos, demo-form fields | Names the target buyer and size; Industry pages; Platform focus (Shopify, enterprise) |
| `breadth` | Product breadth | One module or a suite? What sits next to the core (loyalty, reviews, affiliates, analytics)? | Product menu, pricing feature tables, platform pages | Modules beyond the core; Channels covered |
| `price` | Pricing transparency and model | Is any price public? Model: flat, tiers, revenue bands, usage, % of sales? Trial, free plan, contract length? | Pricing page, app-store listing (often shows a price), third-party comparisons (mark as claims or `demo`) | Price shown on the pricing page; Free plan or trial; Pricing model |
| `proof` | Proof | Named customers with numbers, logos, awards, security badges. Are numbers sourced? | Homepage, customers page, case studies, press | Named customers with a result number; Proof claims carry a source |
| `attack` | Comparison and switching pages aimed at us | Do they publish "X vs us", "alternatives to us", migration guides, switching offers? What do they claim about us? | Site search for our name, `/vs/`, `/compare/`, `/alternatives/`, web search "<them> vs <us>", "<us> alternatives" | Comparison page against us; Migration guide or switching offer; Claims about us that our own pages contradict |
| `onb` | Onboarding and time to value | Self-serve or sales-led? Stated time to go live? Setup steps visible in docs? | Homepage, docs "getting started", app-store listing, review sites (G2 "time to implement", "ease of setup") | States a time to go live; Self-serve setup; Public getting-started docs |
| `integ` | Integrations and ecosystem | Platforms, ESPs, CDPs, app marketplaces; public API docs, webhooks, SDKs, MCP server, partner program | Integrations page, developer docs, app stores, GitHub, MCP registries | Shopify (or main platform) app; Public API docs or MCP server; Partner or agency program |
| `rev` | Reviews | Rating and count per site, with date; recurring praise and complaints; recent trend | G2, Capterra, Software Advice, Trustpilot, Shopify App Store, Apple App Store, Google Play | Rating and count on G2; App-store rating and count; Top complaint themes |
| `seo` | Content and SEO footprint (light) | How big is their footprint, and which topics do they own? Not a deep SEO audit | Tranco rank (tranco-list.eu), sitemap size, blog categories, resource hubs, benchmark reports | Domain rank; Content hub or benchmark report; Top topics |
| `sig` | Hiring and funding signals | Are they investing, and where (sales in a new region, engineering, AI)? Recent rounds, acquisitions, layoffs | Careers page, LinkedIn jobs (public), Crunchbase, press releases | Open roles and where; Funding or M&A in the last 12 months |
| `chg` | Changes over time | What changed in the last 6-12 months: pricing, headline, new pages aimed at us, new products? | Wayback Machine (web.archive.org) snapshots of homepage and pricing; changelog; release notes | Changed pricing or positioning in the last year; New pages aimed at us |

## Judging a cell

- `yes` - clearly present, seen on the page cited.
- `part` - present with a limit (only on the top plan, only for one platform, numbers without names).
- `no` - looked for it (page, site search, sitemap, footer) and it is not there. Say where you looked in the note.
- `nd` - could not check (page blocked, listing not found, tool missing). Never guess.

Keep each row's scale explicit when it is a threshold (ratings: "✓ at 4.5+ with 100+ reviews") and say it in `matrixP`.

## Strategy canvas factors

Pick 5-10 factors that buyers actually compare and that the matrix can support. Name each factor's `basis` (criterion ids). Typical factors for B2B SaaS: price clarity, speed to go live, enterprise depth, named proof, integrations, switching help, suite breadth, review rating, support. Levels 0-10 are judgments; keep them consistent with the cells (a `no` row cannot become an 8).

## ERRC

- **Eliminate**: what we do that buyers do not value or that costs us deals (a gate, a step, a claim no one believes).
- **Reduce**: what we over-serve or over-ask.
- **Raise**: where we are below the best competitor on something buyers weigh.
- **Create**: what no one in the set offers yet and our strengths make credible.

## Moves

A move is a concrete change with an owner type: `page`, `message`, `pricing`, `feature`, `content`, `proof`, `sales`, `data`. It answers named competitors (`vs`) and lists the evidence behind it. Prefer moves the team can ship in weeks; mark bets as `ex`.
