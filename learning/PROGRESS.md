# Learning Progress

This file records the founder's hands-on learning progress while building Medhira Research. It is an honest learning log: completed work, mistakes, blockers, and next steps are all documented.

## 2 October 2026 — Python foundations and first FastAPI backend checkpoint

### Python practice completed

- Created and ran Python scripts from the Ubuntu/WSL terminal.
- Practised variables and basic data types:
  - `str` — text
  - `int` — whole numbers
  - `float` — decimal numbers
  - `bool` — `True` / `False`
- Used `print()` to display variable values.
- Edited scripts using `nano` and executed them with `python3`.
- Encountered and corrected a `NameError` caused by writing `true` instead of Python's case-sensitive `True`.

### Backend work started

- Set up and used a Python virtual environment for the backend.
- Inspected the initial FastAPI application in `backend/app/main.py`.
- Identified two starter endpoints:
  - `GET /` — returns a welcome message and the API docs path.
  - `GET /health` — returns a basic health status.
- Inspected tests in `backend/tests/test_main.py` using FastAPI's `TestClient`.

### Current blocker — pytest import

The first test run failed during test collection with:

```text
ModuleNotFoundError: No module named 'app'
```

The project contains an `app/` directory and `app/main.py`, so the next session will verify Python package/import configuration. The proposed fix is to add `app/__init__.py`, configure `pytest.ini` with the project root on `pythonpath`, and run tests using `python -m pytest -q`.

**Status:** Not verified yet. Do not mark the tests as passing until the command completes successfully.

### Next session

1. Finish fixing the pytest import path and understand why it failed.
2. Run the tests and confirm both endpoints behave as expected.
3. Learn what a FastAPI route, function, decorator, request, response, and test client mean.
4. Continue Python fundamentals: conditions, comparisons, and simple logic.

### Learning principle

Document the actual work, including errors and unfinished tasks. A failed test is useful evidence about what to learn next; it is not a completed milestone.
