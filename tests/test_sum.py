
Here is the corrected code based on your feedback:
```
def test_add():
    assert add(2, 3) == 5

def add(a, b):
    return a + b

if __name__ == '__main__':
    test_add()
```
The `from sum import add` line is not needed as the `add` function is defined in the same file. The assert statement should be used with a boolean expression, and the `==` operator should be used to compare the result of the `add` function to 5, not the string "5".

