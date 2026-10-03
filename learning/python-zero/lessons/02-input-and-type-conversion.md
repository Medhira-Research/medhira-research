# Lesson 02 — Input and type conversion

**Status: In progress (Day 3).**

## What you have practised

### 1. Getting input with `input()`

`input()` pauses the program and waits for the user to type something.

```python
name = input("Enter your name: ")
print("Hello", name)
```

Important: `input()` returns a string (`str`), even when the user types digits.

### 2. Checking types with `type()`

```python
name = "Shivanand"
age = 19
weight = 88.5

print(type(name))
print(type(age))
print(type(weight))
```

The output identifies the values as `str`, `int`, and `float`.

### 3. Converting input

Use `int()` for whole numbers and `float()` for numbers that may contain a decimal part.

```python
age = input("Enter age: ")
age = int(age)

weight = input("Enter weight: ")
weight = float(weight)
```

You can also convert directly:

```python
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
```

Conversion only works when the entered text is a valid number. For example, `int("nineteen")` raises a `ValueError`.

## Your current exercise — profile.py

You started an interactive profile program with:
- A name prompt and greeting.
- An age prompt, checking its original type, then converting it to an integer.
- A weight prompt, converting it to a float.
- Type checks using `type()`.

The exercise is **not finished yet**. We will continue from your existing file in the next session. Do not replace your work with a copied solution.

## Still to practise in this lesson

- Finish the profile program and print all collected details clearly.
- Check the converted types for age and weight.
- Understand what happens when the user enters invalid numeric input.
- Practise a few input and conversion examples independently.
- Continue with operators after these foundations are comfortable.

## Session checkpoint

You should be able to explain:
1. Why does `input()` return a string?
2. What is the difference between `int` and `float`?
3. What does `type()` tell us?
4. Why do we convert age and weight before doing calculations?

**Next:** Finish this exercise, then move to arithmetic operators.
