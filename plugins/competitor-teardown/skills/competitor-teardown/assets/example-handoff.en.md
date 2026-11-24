# Hands-off: Competitor teardown: demo report

Implementation brief generated from a competitor teardown. Work top to bottom: tasks are ordered by ICE, and a task always comes after the ones it depends on. Each task lists the competitor evidence behind it; re-check a source if its date is more than 30 days old. Treat "hypothesis" tasks as experiments: test before building fully.

## Context

- **Main finding:** Kinship sells the switch from Loopwell with a price on the page; Loopwell answers with "Talk to sales"
- Loopwell leads on enterprise depth, fraud controls and review ratings, but it trails on 12 of 17 criteria, nearly all at the evaluation step: no public price, no self-serve setup, no migration help. Kinship has built a comparison page and a migration guide aimed at Loopwell's customers. The cheapest wins are pages and proof, not features.
- **Criteria where we trail the best competitor:** 12 / 17 · **Criteria where we lead outright:** 1
- **Confidence:** 89%

### Products compared

- **Loopwell** (us) — https://loopwell.example — Referral platform for mid-market brands
- **Kinship** — https://kinship.example — Referral and loyalty for Shopify brands
- **Amplo** — https://amplo.example — Enterprise advocacy suite
- **Referrly** — https://referrly.example — Self-serve referral tool for small shops
- **ShareMint** — https://sharemint.example — Reviews and loyalty with a referral add-on

### Where we win

- **Highest review rating of the five** (vs Kinship, Amplo, Referrly, ShareMint). 4.7 on ReviewGrid with support and fraud control as top themes. Sources: ReviewGrid listings (fictional review site) · https://reviewgrid.example/referral-software · checked 2026-11-24
- **Enterprise depth without an enterprise setup bill** (vs Amplo). Public API and webhooks like Amplo, with a Shopify app Amplo lacks. Sources: Loopwell docs · https://loopwell.example/docs · checked 2026-11-24; AppShelf listings (fictional app store) · https://appshelf.example/referral · checked 2026-11-24

### Where we lose

- **No price where buyers compare** (vs Kinship, Referrly, ShareMint). Kinship, Referrly and ShareMint show prices; Loopwell asks for a call. Sources: Loopwell pricing · https://loopwell.example/pricing · checked 2026-11-24; Kinship pricing · https://kinship.example/pricing · checked 2026-11-24; Referrly pricing · https://referrly.example/pricing · checked 2026-11-24; ShareMint pricing · https://sharemint.example/pricing · checked 2026-11-24
- **Kinship owns the comparison** (vs Kinship). A Kinship vs Loopwell page and a migration guide exist; Loopwell has neither. Sources: Kinship vs Loopwell · https://kinship.example/vs/loopwell · checked 2026-11-24; Kinship: migrate from Loopwell · https://kinship.example/guides/migrate-from-loopwell · checked 2026-11-24
- **Referrals only, while three rivals sell suites** (vs Kinship, Amplo, ShareMint). Kinship, Amplo and ShareMint bundle loyalty; Loopwell sells one module. Sources: Kinship homepage · https://kinship.example · checked 2026-11-24; Amplo homepage · https://amplo.example · checked 2026-11-24; ShareMint homepage · https://sharemint.example · checked 2026-11-24

### ERRC

- **Eliminate:** Talk to sales as the only door on the pricing page → T01. Three of four rivals show a price; Loopwell shows none.
- **Reduce:** Required fields on the demo form → T07. Seven fields before any contact; Kinship starts a trial with an email.
- **Raise:** Named proof with numbers → T04. Loopwell's case studies are anonymous while Kinship and Amplo name brands.
- **Raise:** Switching help → T03. Kinship's migration guide targets Loopwell customers; Loopwell offers nothing back.
- **Create:** Fraud-savings report from platform data → T06. Fraud control is Loopwell's top review theme and no rival publishes numbers on it.

### Requester answers and assumptions

- Our product: Loopwell, loopwell.example
- Competitors: Kinship, Amplo, Referrly, ShareMint
- The buyer: Heads of retention at mid-market online brands
- What decision this informs (skipped): Skipped. Assumption: next quarter's website and pricing roadmap

### Sources

1. [ok] Loopwell homepage — https://loopwell.example · checked 2026-11-24
2. [ok] Loopwell pricing — https://loopwell.example/pricing · checked 2026-11-24
3. [ok] Loopwell docs — https://loopwell.example/docs · checked 2026-11-24
4. [ok] Loopwell careers — https://loopwell.example/careers · checked 2026-11-24
5. [ok] Kinship homepage — https://kinship.example · checked 2026-11-24
6. [ok] Kinship pricing — https://kinship.example/pricing · checked 2026-11-24
7. [ok] Kinship vs Loopwell — https://kinship.example/vs/loopwell · checked 2026-11-24
8. [ok] Kinship: migrate from Loopwell — https://kinship.example/guides/migrate-from-loopwell · checked 2026-11-24
9. [ok] Amplo homepage — https://amplo.example · checked 2026-11-24
10. [ok] Amplo pricing — https://amplo.example/pricing · checked 2026-11-24
11. [ok] Amplo careers — https://amplo.example/careers · checked 2026-11-24
12. [ok] Referrly homepage — https://referrly.example · checked 2026-11-24
13. [ok] Referrly pricing — https://referrly.example/pricing · checked 2026-11-24
14. [ok] Referrly alternatives page — https://referrly.example/alternatives · checked 2026-11-24
15. [ok] Referrly help center — https://referrly.example/help · checked 2026-11-24
16. [ok] ShareMint homepage — https://sharemint.example · checked 2026-11-24
17. [ok] ShareMint pricing — https://sharemint.example/pricing · checked 2026-11-24
18. [ok] ReviewGrid listings (fictional review site) — https://reviewgrid.example/referral-software · checked 2026-11-24
19. [ok] AppShelf listings (fictional app store) — https://appshelf.example/referral · checked 2026-11-24
20. [demo] Domain rank list (fictional) — https://rank.example · checked 2026-11-24 · rank only, no traffic
21. [demo] Funding database (fictional) — https://funding.example · checked 2026-11-24 · free tier
22. [ok] Web archive snapshots, Nov 2025 vs Nov 2026 (fictional) — https://archive.example · checked 2026-11-24
23. [ok] Answers at the start (3 of 4)
24. [no] Traffic by channel (Similarweb or similar) — not connected
25. [no] Win/loss reasons from CRM — not shared

Missing, so lower confidence: Traffic by channel (Similarweb or similar), Win/loss reasons from CRM.

## Rules for the implementer

- Do not invent numbers, customers, logos, reviews or quotes. If a claim cannot be sourced, leave it out.
- Anything you publish about a competitor must cite a public URL and the date it was checked; re-check it the day you publish.
- Do not copy competitor text. Quote at most 15 words, in quotation marks, with the source; otherwise paraphrase.
- One vendor's statement about another is a claim, not a fact: never repeat it as fact.
- Do not change public prices, plans or legal terms without the owner's written approval.
- Do not submit real forms, sign up for trials or contact competitors' sales teams while testing.
- When a task is a hypothesis, run the cheapest test first and stop if the threshold is not met.

## Suggested order

| # | ID | Task | Area | Answers | ICE | Type | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | T01 | Show a starting price or an estimator on the pricing page (top 3) | pricing | Kinship, Referrly, ShareMint | 392 | optimize | observed |
| 2 | T02 | Publish a sourced Loopwell vs Kinship page (top 3) | page | Kinship | 392 | optimize | observed |
| 3 | T04 | Name the brands behind both case studies and add one number each (top 3) | proof | Kinship, Amplo | 336 | optimize | observed |
| 4 | T09 | Track pricing to comparison to demo as one funnel | data | — | 280 | optimize | observed |
| 5 | T03 | Switching kit: migration guide and import of existing advocates | content | Kinship | 252 | optimize | hypothesis |
| 6 | T05 | State a go-live number on the homepage, backed by recent launches | message | Kinship, Referrly | 240 | optimize | observed |
| 7 | T07 | Cut the demo form to 3 fields and add calendar booking | sales | Kinship | 200 | optimize | hypothesis |
| 8 | T06 | Annual fraud-savings report from platform data | content | Amplo, Kinship | 120 | explore | hypothesis |
| 9 | T08 | Test a light loyalty module with two current clients | feature | Kinship, ShareMint, Amplo | 56 | explore | hypothesis |

## Tasks

### 1. T01 — Show a starting price or an estimator on the pricing page

- Area: pricing · Answers: Kinship, Referrly, ShareMint · ICE 392 = 8×7×7 · Type: optimize · observed
- Effort: 2–3 days plus a pricing decision

**Why.** Loopwell's pricing page lists three revenue bands and asks for a call in each. Kinship, Referrly and ShareMint show prices; Kinship added an estimator this year.

**Competitor evidence:**

- **Kinship:** Price from $399/month with an order-volume estimator — Kinship pricing · https://kinship.example/pricing · checked 2026-11-24
- **Referrly:** Three plans with monthly prices — Referrly pricing · https://referrly.example/pricing · checked 2026-11-24
- **ShareMint:** Free plan, paid from $199/month — ShareMint pricing · https://sharemint.example/pricing · checked 2026-11-24
- **Kinship:** Estimator added in the last 12 months — Web archive snapshots, Nov 2025 vs Nov 2026 (fictional) · https://archive.example · checked 2026-11-24

**Hypothesis.** If the pricing page shows a starting price, more qualified buyers will book a demo, because three of four rivals already answer the price question.

**Steps:**

1. Pick one honest anchor: a starting price for the smallest band, or a range per band.
2. Add it to the pricing page with what is included and what changes the price.
3. Keep Talk to sales as the second action, not the only one.
4. Run the A/B for 4 weeks and compare qualified demos, not just clicks.

**Acceptance criteria:**

- [ ] Pricing-page demo rate +15% and qualified share not lower than control
- [ ] Metric: Demo requests from the pricing page per 1,000 visits; share qualified by sales

**How to verify:** A/B on the pricing page for 4 weeks: starting price vs current

**Risk / guardrail:** Anchoring too low; publish a starting price that sales already uses.

**Alternatives rejected:**

- Price estimator like Kinship's: stronger, but needs a pricing model sales agrees on; next step if the anchor works.
- Gated price sheet behind email: rejected, buyers read it as hiding.

**Pre-mortem:** It failed because sales kept quoting differently from the page. Agree the anchor with sales before publishing.

**Copy variants:**

- From $1,200 a month for brands up to $20m: anchors the smallest band.
- Most clients pay $1,200–4,000 a month: a range lowers the fear of a high quote.


### 2. T02 — Publish a sourced Loopwell vs Kinship page

- Area: page · Answers: Kinship · ICE 392 = 7×7×8 · Type: optimize · observed
- Effort: ≈1 week

**Why.** Kinship's comparison page targets Loopwell by name and is updated regularly. Loopwell has no comparison page, so buyers who search the two names find only Kinship's version.

**Competitor evidence:**

- **Kinship:** Kinship vs Loopwell page, updated October 2026 — Kinship vs Loopwell · https://kinship.example/vs/loopwell · checked 2026-11-24
- **Loopwell:** Kinship's page says Loopwell has no Shopify app; the app store lists one _(claim by Kinship)_ — Kinship vs Loopwell · https://kinship.example/vs/loopwell · checked 2026-11-24
- **Loopwell:** Loopwell app listed on AppShelf, 4.8 from 64 reviews — AppShelf listings (fictional app store) · https://appshelf.example/referral · checked 2026-11-24

**Hypothesis.** If buyers who read Kinship's page find a sourced answer from Loopwell, fewer will drop Loopwell from the shortlist.

**Steps:**

1. List each claim on Kinship's page and check it against public sources; keep only what you can link.
2. Write a Loopwell vs Kinship page: where each fits, a sourced table and the date checked.
3. Link it from the pricing page and the footer.
4. Re-check the table every quarter and show the date.

**Acceptance criteria:**

- [ ] The page reaches the first results for the two names within 8 weeks and brings 5+ demos
- [ ] Metric: Organic entries to the page and demo requests from it

**How to verify:** Publish one page, link it from pricing, compare demos 6 weeks before and after

**Risk / guardrail:** Claims about a rival go stale; date every row and never state their price unless it is public.

**Alternatives rejected:**

- Reply in sales decks only: rejected, buyers search before they talk to sales.
- Ask Kinship to correct the Shopify claim: worth doing as well, but does not answer the buyer.

**Pre-mortem:** It failed because the page read as an attack. Lead with where each product fits, and keep the tone factual.


### 3. T04 — Name the brands behind both case studies and add one number each

- Area: proof · Answers: Kinship, Amplo · ICE 336 = 6×7×8 · Type: optimize · observed
- Effort: 1–2 weeks, mostly waiting for approvals

**Why.** Both Loopwell case studies say a beauty brand and a fashion retailer. Kinship and Amplo name the brand and give one number each.

**Competitor evidence:**

- **Kinship:** Six named brands with one result each — Kinship homepage · https://kinship.example · checked 2026-11-24
- **Amplo:** Named enterprise cases with ROI figures — Amplo homepage · https://amplo.example · checked 2026-11-24

**Hypothesis.** If case studies name the brand and one number, the homepage will earn more demo clicks, because buyers trust named proof more.

**Steps:**

1. Ask the two featured clients for permission to name them.
2. Add the brand, one number and the period to each case.
3. Put the best number in the homepage hero.

**Acceptance criteria:**

- [ ] Case-study click rate +20% in 4 weeks
- [ ] Metric: Homepage click rate on case studies; demo requests

**How to verify:** Ask the two featured clients for permission; swap and compare 4 weeks

**Risk / guardrail:** Clients say no; offer review rights and pick others with public results.

**Alternatives rejected:**

- Anonymous numbers in the hero: rejected, the gap is trust, not numbers.
- Video testimonials: later, slower to produce.

**Pre-mortem:** It failed because legal teams took 3 months. Start with clients who already spoke at events.


### 4. T09 — Track pricing to comparison to demo as one funnel

- Area: data · Answers: — · ICE 280 = 5×8×7 · Type: optimize · observed
- Effort: 2 days

**Why.** No analytics data was available for this teardown, so the effect of the page moves cannot be measured yet.

**Competitor evidence:**

- **Kinship:** Kinship's estimator and vs page sit on the same path a buyer takes — Kinship pricing · https://kinship.example/pricing · checked 2026-11-24

**Steps:**

1. Tag pricing, comparison and demo pages as one funnel.
2. Report weekly: visits, demo requests, qualified demos.
3. Re-run this teardown with the data.

**Acceptance criteria:**

- [ ] Metric: Funnel tracked end to end

**Risk / guardrail:** Double-counted events; test in a staging property first.


### 5. T03 — Switching kit: migration guide and import of existing advocates

- Area: content · Answers: Kinship · ICE 252 = 7×6×6 · Type: optimize · hypothesis
- Effort: ≈2 weeks

**Why.** Kinship publishes a step-by-step guide for leaving Loopwell. Loopwell's docs have no guide for brands leaving other tools.

**Competitor evidence:**

- **Kinship:** Migration guide aimed at Loopwell customers — Kinship: migrate from Loopwell · https://kinship.example/guides/migrate-from-loopwell · checked 2026-11-24
- **Referrly:** CSV import of existing advocates — Referrly help center · https://referrly.example/help · checked 2026-11-24

**Steps:**

1. Write one migration guide per main rival: export, mapping, codes, go-live checklist.
2. Build an import for existing advocates and referral codes.
3. Offer a migration call in the guide.

**Acceptance criteria:**

- [ ] Metric: Deals that mention switching from a rival

**Risk / guardrail:** Promising a migration the team cannot staff; cap free migrations per month.


### 6. T05 — State a go-live number on the homepage, backed by recent launches

- Area: message · Answers: Kinship, Referrly · ICE 240 = 5×6×8 · Type: optimize · observed
- Effort: 1 day

**Why.** The homepage says weeks without a number. Kinship says 7 days and Referrly says 10 minutes.

**Competitor evidence:**

- **Kinship:** Live in 7 days for Shopify stores — Kinship homepage · https://kinship.example · checked 2026-11-24
- **Referrly:** 10 minutes to launch — Referrly homepage · https://referrly.example · checked 2026-11-24

**Steps:**

1. Take the median go-live time of the last 10 launches.
2. State it on the homepage with what it includes.
3. Track it every month.

**Acceptance criteria:**

- [ ] Metric: Median days to go live; homepage demo rate

**Risk / guardrail:** Stating a number the team misses; use the median, not the best case.


### 7. T07 — Cut the demo form to 3 fields and add calendar booking

- Area: sales · Answers: Kinship · ICE 200 = 5×5×8 · Type: optimize · hypothesis
- Effort: 1–2 days

**Why.** Loopwell's demo form asks seven fields before any contact. Kinship starts a trial with an email address.

**Competitor evidence:**

- **Kinship:** Trial starts with an email address — Kinship pricing · https://kinship.example/pricing · checked 2026-11-24

**Steps:**

1. Keep name, work email and company; move the rest to the call.
2. Add calendar booking after submit.
3. Compare completion and qualified share for 4 weeks.

**Acceptance criteria:**

- [ ] Metric: Form completion rate and qualified share

**Risk / guardrail:** More unqualified demos; qualify on the call.


### 8. T06 — Annual fraud-savings report from platform data

- Area: content · Answers: Amplo, Kinship · ICE 120 = 6×5×4 · Type: explore · hypothesis
- Effort: ≈3 weeks

**Why.** Fraud control is the top theme in Loopwell's reviews and none of the four rivals publishes fraud numbers.

**Competitor evidence:**

- **Loopwell:** Fraud control among top review themes — ReviewGrid listings (fictional review site) · https://reviewgrid.example/referral-software · checked 2026-11-24
- **Amplo:** Publishes research reports, none on fraud — Amplo homepage · https://amplo.example · checked 2026-11-24

**Steps:**

1. Aggregate blocked referrals across clients for 12 months, anonymized.
2. Publish a short report with method and limits.
3. Use it as the offer for visitors not ready for a demo.

**Acceptance criteria:**

- [ ] Metric: Report downloads and demos from them

**Risk / guardrail:** Client data: aggregate only, legal review before publishing.


### 9. T08 — Test a light loyalty module with two current clients

- Area: feature · Answers: Kinship, ShareMint, Amplo · ICE 56 = 7×4×2 · Type: explore · hypothesis
- Effort: 3 months

**Why.** Kinship, Amplo and ShareMint sell loyalty with referrals; Loopwell sells referrals only. Whether Loopwell's buyers want a suite is unknown.

**Competitor evidence:**

- **Kinship:** Points, tiers and referrals — Kinship homepage · https://kinship.example · checked 2026-11-24
- **ShareMint:** Referral add-on moved into every paid plan — Web archive snapshots, Nov 2025 vs Nov 2026 (fictional) · https://archive.example · checked 2026-11-24

**Steps:**

1. Ask 8 clients what they use for loyalty and what they pay.
2. If 3+ would switch, build the smallest points feature with two clients.
3. Decide after 3 months.

**Acceptance criteria:**

- [ ] Metric: Clients willing to pilot; retention of pilot clients

**Risk / guardrail:** Splitting focus before the evaluation-stage gaps are fixed.

## Glossary

- **ICE** (priority score): Impact × Confidence × Ease, each 1–10. The bigger the product, the sooner to do it.
- **ERRC** (eliminate, reduce, raise, create): The Blue Ocean grid: what to drop, cut, push above the industry and add that nobody offers.
- **Blue Ocean** (compete where others do not): Strategy of making the competition irrelevant by offering a different mix of value rather than more of the same.
- **strategy canvas** (offering levels side by side): A line per product across the factors buyers compare. Where lines run together nobody wins; gaps show where to differ.
- **pre-mortem** (failure analysis in advance): Imagine the move failed in 3 months and explain why. The reasons become risks to close now.
- **A/B** (split test): Half the visitors see the new version, half the old one; the difference shows the effect.
- **MCP** (connector for AI agents): Model Context Protocol: a standard way for AI assistants to use a product's data and actions.
- **API** (programmatic access): A documented way for other software to read and change data in the product.
- **ROI** (return on investment): What a program earns compared with what it costs.
- **Shopify Plus** (Shopify's enterprise plan): The plan larger Shopify stores use; a common size signal in ecommerce.
