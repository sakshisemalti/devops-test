# AI refactor applied
```
Here's the corrected code:
```
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except TypeError as e:
        if not isinstance(a, int):
            raise ValueError("a must be an integer")
        elif not isinstance(b, int):
            raise ValueError("b must be an integer")
        else:
            raise e
    return result
```
This corrected code handles the case where `a` or `b` is not an integer by raising a `ValueError`. It also provides a meaningful error message for each of these cases. The `try-except` block catches any errors that may occur during the execution of the `add()` function, and it raises a more informative error message if an error occurs.

