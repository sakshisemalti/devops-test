# AI refactor applied

The code you provided is not valid Python. The `from sum import add` line is not needed, as the `add` function is already defined in the same file. Additionally, the `assert` statement should be used with a boolean expression, and the `==` operator should be used to compare the result of the `add` function to 5, not the string "5".

Here's the corrected code:
```python
def test_add():
    assert add(2, 3) == 5

def add(a, b):
    return a + b
```

