# Contributing

Thanks for your interest in contributing.

## Setup

```bash
git clone <repo-url>
cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python app.py
```

## Quality gate

```bash
python -m pytest -q
```

CI runs the test suite on every push/PR.

## Process

1. Branch from `main`: `feat/my-feature` or `fix/my-bug`.
2. Add a test in `tests/` for new behavior.
3. Run `python -m pytest -q`.
4. Commit with a Conventional Commit message and open a PR.

## PR checklist

- [ ] `pytest` passes
- [ ] Tests added/updated
- [ ] README updated if behavior changed