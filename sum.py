# AI refactor applied
def add(a: int, b: int) -> int:
    try:
        return a + b
    except ZeroDivisionError:
        print("Cannot divide by zero")