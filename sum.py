# AI refactor applied
```
Here's the corrected code:
```
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except TypeError as e:
        raise ValueError("Input parameters must be integers") from e
    return result
```
The `try` block is used to handle the exception thrown when trying to add a non-integer value to an integer. The `except` block catches the exception and raises a new error with a more informative message. The `from` clause is used to specify that the original exception should be propagated as the cause of the new error.

Also, the return type of the function is changed from `None` to `int`, since the function now returns an integer value.

