# AI refactor applied
import sys
from typing import Any, Optional
def add(a: int, b: int) -> int:
    try:
        return a + b
    except TypeError as e:
        print("Invalid input. Please enter two integers.", file=sys.stderr)
        return 0
    except ZeroDivisionError as e:
        print("Cannot divide by zero.", file=sys.stderr)
        return 0