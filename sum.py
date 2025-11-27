  Sure, here's the corrected code based on the test failures you provided:
```
def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input. Both 'a' and 'b' must be integers.")
    return a + b
```
This code uses the `isinstance` function to check that both inputs are of type `int`, and raises a `ValueError` with a specific message if this condition is not met. The return type of the function is now specified as `int`, which ensures that the function always returns an integer value when both inputs are valid integers.

This corrected version of the code should be more robust and user-friendly in the face of unexpected input values, and it should also match the behavior of the previous version of the code.

