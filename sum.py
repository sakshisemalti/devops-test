# AI refactor applied
def add(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Inputs must be integers") from e

Additionally, this code uses the `from` clause to specify the original exception as the cause of the new exception. This helps to maintain a clear chain of exceptions and provides more information about the cause of the error.