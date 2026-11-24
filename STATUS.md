# Status

Living state of the work. Update at the end of every session. Public repo: no real site names, client data or private links here.

**Version:** 1.0.0 (2026-11-24)

## Done recently

- First release: 12 lenses, sourced comparison matrix, strategy canvas, ERRC, positioning map, win/lose, ICE-ranked moves; report + hands-off file from one `audit.json`; validate, build, hands-off and render-check scripts; English demo with fictional companies.
- Validator rules: dated source on every cell, rival claims marked as claims, quotes up to 15 words, competitor evidence on every move, top-3 rules.
- Test run on a real B2B SaaS vs 4 competitors (public data), then with the owner's GA4 and Search Console mid-run. An independent fact check corrected 15 of 101 cells. Lessons added to `SKILL.md`: read page text (not fetch summaries), check the footer before "none found", one source per URL, read every product's case-studies page, audit only production domains.
- Repo docs: `CLAUDE.md`, `STATUS.md`.

## In progress

- Nothing open in this repo.

## Next

1. Maintainer: create tag v1.0.0 and a GitHub Release (the session cannot push tags), and share the demo artifact publicly.
2. Test install in Claude Code desktop and in the Claude app (upload the ZIP).
3. Run trigger evals from `evals/trigger-evals.json` with the skill-creator skill.
4. Ukrainian demo (`example-teardown.json`, `lang: uk`) and a Ukrainian check of all template labels.
5. Second test in another category (e-commerce app or a mobile app with app-store reviews only).
6. Add a "previous teardown" diff: compare two `audit.json` files and show what changed per competitor.

## Open questions

- Should a validator rule reject sources on a non-production subdomain of a listed product (to enforce the production-domain rule mechanically)?
- Move the shared report core into its own repo once more sibling skills exist?

## Links

- Public demo: EN https://claude.ai/artifact/SHTuw2y1ofKtEzbpHR2QVM (fictional companies)
- Reference repo: https://github.com/artemhorbenko/product-lens-audit
