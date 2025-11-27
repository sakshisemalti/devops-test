# AI refactor applied
  This is not a valid Python code. There are several errors in the code:

1. The function name should be in lowercase, so it should be `add(a, b)` instead of `Add(a, b)`.
2. The return statement should not have a semicolon at the end.
3. The try-except block is not closed properly. It should be `except ZeroDivisionError:` instead of `except ZeroDivisionError:`.
4. The print statement inside the except block should not have parentheses.
5. There should be a colon after the function name and parameter list in the function definition.

Here's the corrected code:
```
def add(a, b):
    try:
        return a + b
    except ZeroDivisionError:
        print("Cannot divide by zero")
```

