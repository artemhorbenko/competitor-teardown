# competitor-teardown — notes for Claude and contributors

Start every session by reading this file and STATUS.md, then continue from Next. End every session by updating STATUS.md and committing.

A public Claude skill (Claude Code plugin + Claude app skill ZIP) that compares a product with up to five competitors from public pages and review sites through the same 12 lenses, cites a URL and a checked-on date for every matrix cell, and outputs two files from one `audit.json`: a visual HTML report for people (comparison matrix, strategy canvas, ERRC, positioning map, win/lose, ICE-ranked moves) and a Markdown hands-off brief for AI agents.

## Layout

```
.claude-plugin/marketplace.json        this repo is a plugin marketplace
plugins/competitor-teardown/           the only folder that ships to users
  .claude-plugin/plugin.json
  skills/competitor-teardown/
    SKILL.md                           the process Claude follows
    references/                        lenses, data sources, report spec, audit.schema.json
    assets/                            report-template.html, example teardown (fictional), example hands-off
    scripts/                           validate_audit, build_report, build_handoff, check_report
evals/                                 scenarios, trigger prompts, results log (anonymised)
docs/                                  README screenshots
competitor-teardown-skill.zip          Claude app upload, rebuilt on every skill change
CLAUDE.md, STATUS.md, CHANGELOG.md     repo docs; never move them into plugins/
```

## Rules

- Respond to the maintainer in Ukrainian; code, docs and commits in English.
- Never invent numbers. Missing data shows as "no data" (`nd`) and lowers confidence.
- Audit only the production domain of each product the user names; ignore other subdomains found via search (old landing pages, A/B or staging hosts) unless the user confirms they are live.
- Every matrix cell cites a public URL and a checked-on date. One vendor's words about another are a claim (`claim: true`), never a fact. Quote competitors in at most 15 words.
- Real teardowns stay private (artifacts or local files). Nothing in this repo may name a real audited product, client data or private links; log runs in `evals/results.md` anonymised.
- Public demos use fictional products only (`.example` domains).
- Claude writes only `audit.json`; the template and scripts render everything. Change the template, not the data, when layout breaks.
- Keep `SKILL.md` short; details go to `references/`.
- Use data sources read-only. Never submit real forms, sign up for trials, request demos, or contact anyone at a competitor.

## Build and check

```
S=plugins/competitor-teardown/skills/competitor-teardown
python $S/scripts/validate_audit.py audit.json
python $S/scripts/build_report.py audit.json report.html
python $S/scripts/build_handoff.py audit.json handoff.md --json tasks.json
python $S/scripts/check_report.py report.html --out ./report-check   # needs playwright + Chromium
```

Before committing a template or script change, run all four on `assets/example-teardown.en.json`, regenerate `assets/example-handoff.en.md`, refresh the embedded demo in `report-template.html`, and check that a deliberately broken input (a cell without a source, a 20-word quote, a rival claim without `claim: true`) fails validation.

## Release

1. Bump the version in `.claude-plugin/marketplace.json` and `plugins/competitor-teardown/.claude-plugin/plugin.json`.
2. Add a section to `CHANGELOG.md` (user-facing changes only).
3. Rebuild the ZIP: `cd plugins/competitor-teardown/skills && rm -f ../../../competitor-teardown-skill.zip && zip -qr ../../../competitor-teardown-skill.zip competitor-teardown -x '*/__pycache__/*'`
4. `claude plugin validate .`
5. Commit and push; tags and GitHub releases are created by the maintainer.

## Related repos

Same report core and design: `product-lens-audit` (the reference; shared core changes are made there first, then copied), `seo-audit`, `qa-audit`, `ui-review`, `ux-review` (all under github.com/artemhorbenko).
