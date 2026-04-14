import pytest
from calculator import add

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(5,5) == 10
    assert add(3,7) == 10

@pytest.mark.parametrize("a,b,expected", [
    (10,5,15)
    (-10,-5,-15)
    (1.5,2.5,4.0)])
def test_add_complex(a,b,expected):
    assert add(a,b) == expected
