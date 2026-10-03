# Python Learning Log

A practical, from-zero Python learning track maintained as part of Medhira Research.

## Current status

- **Current stage:** Python foundations
- **Latest session:** Revision after Day 3
- **Status:** Paused here; resume with the next revision exercise
- **Goal:** Become comfortable writing Python independently, understanding program logic, and building toward backend development with FastAPI, deployment, Docker, cloud, and job-ready projects.

## Concepts covered so far

- Variables and assigning values
- Printing output with `print()`
- Reading user input with `input()`
- Python's basic data types: `str`, `int`, and `float`
- Checking types with `type()`
- Converting input with `int()` and `float()`

## Latest revision exercise

File: `revision.py`

```python
name = input("Enter name: ")
print("Hello", name)
print(type(name))

age = input("Enter age: ")
age = int(age)
print("Your age:", age)
print(type(age))

weight = input("Enter weight: ")
weight = float(weight)
print("Your weight:", weight)
print(type(weight))
```

### What this demonstrates

- `input()` returns a string, even when the user types digits.
- `int()` converts a whole-number string such as `"19"` to an integer.
- `float()` converts numeric input such as `"88"` to a floating-point value (`88.0`).
- `type()` displays the value's Python type.
- `int("25.5")` raises `ValueError`; a decimal-formatted string cannot be converted directly to an integer.

## Next session

1. Finish the revision challenge by collecting name, age, weight, and college name and printing each value with its type.
2. Review variables, input/output, data types, and type conversion without copying notes.
3. Continue with operators and small logic exercises only after these foundations feel comfortable.

## Learning principle

Understand the logic, type the code yourself, run it, inspect errors, and explain what each line does. Progress is measured by what you can build independently—not by how quickly you finish days.
