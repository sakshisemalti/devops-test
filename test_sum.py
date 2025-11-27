# AI refactor applied

Here is the refactored code with the bug fixed:
```
from sum import add

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
```
The original code was missing the second assertion statement, which checks the behavior of the `add` function with negative inputs.

Also note that it is a good practice to test your functions with different input values and expected output values to ensure that they are working correctly.

