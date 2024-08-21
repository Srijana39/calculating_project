from app import add, subtract

def test_add_positive():
    assert add(1, 2) == 3  # This test will pass

def test_add_negative():
    assert add(-1, -2) == -3  # This test will pass

def test_subtract_positive():
    assert subtract(5, 3) == 2  # This test will pass

def test_add_fail():
    assert add(1, 1) == 3  # This test will fail

def test_subtract_fail():
    assert subtract(10, 5) == 8  # This test will fail
