# Python from Zero — Medhira Research

A practical, exercise-first Python course for absolute beginners. This is the first stage of the Medhira Hub backend engineering track.

## How to learn here

1. Follow the lessons in order.
2. Type every example yourself. Do not just copy and paste.
3. Complete the exercises before looking for solutions.
4. Commit your work with a meaningful Git message.
5. Ask questions by opening a GitHub issue. Include the lesson, what you expected, what happened, and the full error message (remove secrets).

## Learning environment

Use Python 3.11 or newer. On Ubuntu/WSL:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git
python3 --version
```

Create and activate a virtual environment from this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`.

## Lessons

| Lesson | Topic | Status |
|---|---|---|
| 00 | Setup, terminal, running your first Python file | Completed in guided session |
| 01 | print, comments, variables and basic types | In progress — complete the profile exercise and `type()` checks |
| 02 | Input, type conversion and operators | Next session |
| 03 | Conditions | Planned |
| 04 | Loops | Planned |
| 05 | Strings and collections | Planned |
| 06 | Functions | Planned |
| 07 | Files and exceptions | Planned |
| 08 | Modules, packages and virtual environments | Planned |
| 09 | Object-oriented programming | Planned |
| 10 | HTTP, JSON and calling APIs | Planned |
| 11 | SQLite and a first data-backed application | Planned |
| 12 | Build the command-line Research Tracker | Planned |

## First project: Research Tracker CLI

You will gradually build a terminal application to record research projects, tasks, experiment notes and results. Each lesson adds one capability. Later, we will turn the same domain into a FastAPI backend.

## Rules

- Understand before moving on.
- Prefer small working commits.
- Never commit passwords, API keys, tokens, datasets you do not have rights to share, or private research data.
- AI can explain, review and quiz you; you must be able to explain every line you submit.

## CI

GitHub Actions runs the automated checks for this learning project whenever relevant files change. A green check means the configured checks passed; it does not replace understanding the code.
