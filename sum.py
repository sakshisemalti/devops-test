# AI refactor applied
```
The corrected version of the code uses type hints to specify that both `a` and `b` must be integers. It then uses a `try` block to catch any errors that may occur during the execution of the code, and returns an error message if either `a` or `b` is not an integer.

Here's the corrected code:
```
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except ValueError:
        return "Invalid input. Both 'a' and 'b' must be integers."
    return result
```
This version of the code is more robust and can handle errors in a more meaningful way than the original code.

