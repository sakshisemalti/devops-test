# AI refactor applied

Here is the corrected version of the code:
```
def test_add():
    assert add(2, 3) == 5

def add(a, b):
    return a + b
```
Explanation:
The original code had an indentation error in the `test_add()` function. The `assert` statement was not indented properly, which caused a syntax error. Additionally, there was a missing colon after the `def add(a, b)` line, which also caused a syntax error.

After fixing these issues, the code should run without any errors and produce the expected output.

