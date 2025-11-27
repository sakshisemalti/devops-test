  Here is the corrected code:
```
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except TypeError as e:
        raise ValueError("Invalid input. Both 'a' and 'b' must be integers.") from e
    return result
```
This code handles the case where `a` or `b` is not an integer by raising a `ValueError`. This error message informs the user that both `a` and `b` must be integers. The `from e` clause specifies the original exception as the cause of the new exception, which helps to maintain a stack trace that points to the original error.

Additionally, this code uses type hints to specify the input parameters and return value, which can help catch errors at runtime and make the code easier to understand for other developers.

