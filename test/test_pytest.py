from src.calculator import fun1, fun2, fun3, fun4


def test_fun1():
    assert fun1(5, 3) == 8


def test_fun2():
    assert fun2(5, 3) == 2


def test_fun3():
    assert fun3(5, 3) == 15


def test_fun4():
    assert fun4(5, 3) == 25