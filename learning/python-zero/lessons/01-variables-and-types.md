# Lesson 01 — Variables and basic data types

## Goal

Learn how to store information in variables and recognise Python's four basic data types.

## 1. Variables

A variable is a name that refers to a value.

```python
name = "Nandu"
age = 19
weight = 88.5
is_learning_backend = True
```

Python executes assignments from top to bottom. Assigning a new value to an existing variable changes the value it refers to.

## 2. The basic types

| Type | Example | Used for |
|---|---|---|
| `str` | `"Nandu"` | Text |
| `int` | `19` | Whole numbers |
| `float` | `88.5` | Decimal numbers |
| `bool` | `True`, `False` | Yes/no or true/false states |

Quotation marks matter: `"19"` is a string, while `19` is an integer.

Check a value's type with `type()`:

```python
age = 19
print(type(age))
```

## 3. Python is case-sensitive

Python distinguishes uppercase and lowercase letters.

```python
is_active = True
is_finished = False
```

Writing `true` instead of `True` causes a `NameError`, because `true` is not Python's Boolean literal.

## 4. Practise

Create `day2.py`:

```python
name = "Nandu"
age = 19
weight = 88.5
is_learning_backend = True

print(name)
print(age)
print(weight)
print(is_learning_backend)

print(type(name))
print(type(age))
print(type(weight))
print(type(is_learning_backend))
```

Run it:

```bash
python3 day2.py
```

## Exercises

1. Create `researcher.py` with variables for your name, university, organisation, primary skill, current level, projects completed, and collaboration availability.
2. Print a readable researcher profile.
3. Print the type of each variable using `type()`.
4. Change one value and run the program again. Observe the result.
5. Explain why `age = "19"` and `age = 19` are different.

## Debugging checkpoint

Try `backend = true` and read the error. Then correct it to `backend = True`.

Errors are useful feedback. Read the final line and the line number in the traceback before changing code.

**Next:** Lesson 02 — input, type conversion and operators.
