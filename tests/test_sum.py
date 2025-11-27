  Here is the refactored code with some bug fixes:
```
def test_add():
    assert add(2, 3) == 5

def add(a, b):
    return sum(a, b)
```
Explanation:

1. The `test_add()` function is not necessary, as the `assert` statement will automatically run the `add()` function and check if it returns the correct result.
2. The `if __name__ == "__main__":` block is not needed, as this is only used to run the script directly (e.g., `python my_script.py`), but in this case we are just testing a function so it's not necessary.
3. The `add()` function can be simplified by using the built-in `sum()` function:
```
def add(a, b):
    return sum(a, b)
```
This will also fix a potential bug in the original code where the `add()` function was not returning the correct result if the input values were negative.

