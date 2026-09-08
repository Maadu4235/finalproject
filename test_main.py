from main import A,B,C

def test_A():
    assert A() == "first function"
def test_B():
    assert B() == "second function"
def test_C():
    assert C(1,2) == 3
