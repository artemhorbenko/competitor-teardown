# Evals

- `evals.json` - end-to-end scenarios: what the run must do (`expectations`) and must not do (`forbidden`). Run each in a fresh session with the plugin installed, then grade the result against the lists.
- `trigger-evals.json` - prompts that should and should not start the skill. With the skill-creator skill installed, ask it to run trigger evals on `plugins/competitor-teardown/skills/competitor-teardown` with this file.
- `results.md` - one row per run.

Every report must also pass the automatic checks:

```
S=plugins/competitor-teardown/skills/competitor-teardown
python $S/scripts/validate_audit.py audit.json
python $S/scripts/build_handoff.py audit.json handoff.md --json tasks.json
python $S/scripts/check_report.py report.html
```

Real products stay private: record the scenario and the scores here, not the names or the data.
