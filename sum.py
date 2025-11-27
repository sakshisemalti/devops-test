# AI refactor applied
In addition, the function now ensures that both `a` and `b` are integers before attempting to add them together. This is done using the `isinstance` method, which checks if an object is an instance of a specific class. In this case, we check if `a` and `b` are instances of the `int` class. If they are not, a `ValueError` will be raised with a message indicating that only integers can be added.

def add(a: int, b: int) -> int:
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Only integers can be added")
        return a + b
    except ValueError as e:
        print(e)