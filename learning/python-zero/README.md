# Python from Zero — Medhira Research

A practical, exercise-first Python course for absolute beginners. This is the first stage of the Medhira Hub backend engineering track.

## How to learn here

1. Follow the lessons in order.
2. Type every example yourself. Do not just copy and paste.
3. Complete the exercises before looking for solutions.
4. Commit your work with a meaningful Git message.
5. Ask questions by opening a GitHub issue. Include the lesson, what you expected, what happened, and the full error message (remove secrets).

## Daily coding practice

Python learning is connected to competitive-programming practice from the beginning.

**Target: one problem per day.**

Use the platform whose problem difficulty matches the concepts currently learned. Do not jump into advanced DSA just because a platform contains it.

Practice platforms:
- HackerRank — https://www.hackerrank.com/
- LeetCode — https://leetcode.com/
- CodeChef — https://www.codechef.com/
- Codeforces — https://codeforces.com/

### Practice progression

| Python stage | Recommended practice |
|---|---|
| Day 1–2 | Very easy output, variables, arithmetic and basic implementation problems |
| Day 3–4 | Input, type conversion, operators and simple conditions |
| Conditions + loops | Easy implementation, counting and simulation |
| Strings + collections | String/array/hash-map basics |
| Functions | Small reusable-solution problems |
| DSA topics | Platform problems matched to the DSA topic being studied |

### Daily problem rule

For each daily problem:

1. Read the problem yourself.
2. Try for at least 20–30 minutes.
3. Write the solution yourself.
4. Run sample tests.
5. Submit it.
6. If stuck, study the concept—not just the final code.
7. Be able to explain your solution afterward.

**One solved problem is enough for the day. Consistency matters more than problem count.**

Keep competitive-programming solutions separate from the teaching examples in this course.

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
| 00 | Setup, terminal, running your first Python file | Completed |
| 01 | print, comments, variables and basic types | Restarting from Day 1 |
| 02 | Input, type conversion and operators | Planned |
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
- Competitive-programming practice is part of the learning routine, but one good solution is better than mindlessly grinding many problems.

## CI

GitHub Actions runs the automated checks for this learning project whenever relevant files change. A green check means the configured checks passed; it does not replace understanding the code.
