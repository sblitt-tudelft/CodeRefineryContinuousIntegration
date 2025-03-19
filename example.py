def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do so.

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add("spec", "tacular") == "spectacular"