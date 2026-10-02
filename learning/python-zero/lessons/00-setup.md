# Lesson 00 — Set up and run Python

## Goal

By the end, you can open a terminal, check your Python installation, create a Python file, run it, and explain what happened.

## 1. Check Python

On Ubuntu or WSL:

```bash
python3 --version
```

If the command is missing:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

## 2. Make your workspace

```bash
mkdir -p ~/medhira-learning/python-zero
cd ~/medhira-learning/python-zero
```

A directory is a folder. `mkdir` creates one; `cd` moves into it; `pwd` prints your current location; `ls` lists its contents.

Try:

```bash
pwd
ls
```

## 3. Your first Python program

Create a file:

```bash
nano hello.py
```

Type this yourself:

```python
print("Hello, Medhira Research!")
print("I am learning Python from zero.")
```

Save in nano with Ctrl+O, Enter, then Ctrl+X.

Run it:

```bash
python3 hello.py
```

## What happened?

- `hello.py` is a text file containing Python instructions.
- `print()` tells Python to display something.
- The text inside quotation marks is a string.
- Python executes the instructions from top to bottom.

## Exercises

1. Change the first message to include your name.
2. Add a third `print()` line describing what you want to build.
3. Create `about.py` and print three lines about Medhira Research.
4. Run both files from the terminal.

## Check your understanding

Answer these without searching:

1. What is a terminal?
2. What is a Python file?
3. What does `print()` do?
4. What is the difference between a folder and a file?
5. Why do we run `python3 hello.py`?

## Completion criteria

You can create and run both files without following the commands line by line. Commit your completed exercises to your own learning branch or fork.

**Next:** Lesson 01 — print, comments, variables and basic data types.
