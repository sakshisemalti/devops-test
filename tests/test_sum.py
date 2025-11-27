# AI refactor applied
# Refactored code
def test_add():
    assert add(2, 3) == 5

def add(a: int, b: int) -> int:
    return a + b