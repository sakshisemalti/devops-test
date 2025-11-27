# AI refactor applied

Here's the fixed code:
```
def add(a: int, b: int) -> int:
    try:
        result = a + b
    except TypeError as e:
        raise ValueError("Input must be integers") from e
    return result
```
Explanation:

* The `try` block is used to handle the case where either `a` or `b` is not an integer. If either of them is not an integer, a `TypeError` will be raised, which will be caught by the `except` block.
* In the `except` block, we raise a more meaningful error message by using the `ValueError` exception and adding a custom message to it. We also use the `from e` syntax to preserve the original error information.
* Finally, we return the result of the addition operation, which will be an integer if both `a` and `b` are integers.

