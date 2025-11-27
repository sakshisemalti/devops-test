  Here is the refactored code with the bug fixed:
```
from sum import add

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
```
The original code was missing the second assertion statement, which checks the behavior of the `add` function with negative inputs.

Also note that it is a good practice to test your functions with different input values and expected output values to ensure that they are working correctly.

It's important to test our code thoroughly to ensure that it works as intended and that all the edge cases have been covered. This helps us catch any bugs or errors in the code before it is used by others, making our code more reliable and maintainable.

