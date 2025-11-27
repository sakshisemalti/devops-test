# AI refactor applied
[PYTHON]
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except TypeError as e:
        raise ValueError("Invalid input. Both 'a' and 'b' must be integers.") from e
    return result
[/PYTHON]
```
This version of the code uses a `try-except` block to handle the case where either `a` or `b` is not an integer. If an error occurs during the addition, the except block will catch it and raise a more informative error message, which is a `ValueError` with a specific message.

Additionally, the return type of the function is now specified as `int`, which ensures that the function always returns an integer value when both inputs are valid integers.

This corrected version of the code should be more robust and user-friendly in the face of unexpected input values.

