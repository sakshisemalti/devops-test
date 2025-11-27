  Sure! Here is the corrected code based on the provided test failures:
```
def add(a, b):
    try:
        return a + b
    except ZeroDivisionError:
        print "Cannot divide by zero"
```
The corrected code includes the following changes:
1. The function name should be in lowercase, so it should be `add(a, b)` instead of `Add(a, b)`.
2. The return statement should not have a semicolon at the end.
3. The try-except block is not closed properly. It should be `except ZeroDivisionError:` instead of `except ZeroDivisionError:`.
4. The print statement inside the except block should not have parentheses.
5. There should be a colon after the function name and parameter list in the function definition.

