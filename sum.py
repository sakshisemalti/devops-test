# AI refactor applied
def add(a: int, b: int) -> int:
    try:
        return a + b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
        return 0