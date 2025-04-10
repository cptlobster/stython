from stython.decorators import typecheck
import pytest
from typing import List

@typecheck
def f1(a: int, b: int) -> int:
    if isinstance(a, str):
        a = len(a)
    if isinstance(b, str):
        b = len(b)
    return a + b

@typecheck
def f2(a: str) -> int:

    return len(a)

@typecheck
def f3(a: str) -> int:
    """this function intentionally returns an incorrect type so we can test return type checking"""
    return a

@typecheck
def f4(*a: List[int]) -> int:
    """this test handles a starred list of arguments"""
    result = 0
    for i in a:
        if isinstance(i, str):
            result += len(i)
        else:
            result += i
    return result

@typecheck
def f5(a: int, b: int, subtract: bool = False, multiply: bool = False) -> int:
    """This test is for named parameters with default values"""
    if subtract:
        return a - b
    if multiply:
        return a * b
    else:
        return a + b

@typecheck
def f6(a: int):
    """This function returns nothing, to test returning a NoneType"""
    pass

@typecheck
def f7() -> int:
    """This function takes no arguments, and should not trigger type errors"""
    return 0

def test_arguments():
    assert f1(1, 1) == 2
    assert f2("hello") == 5

def test_fail_on_bad_argument():
    with pytest.raises(TypeError):
        f1(2, "beans")

def test_fail_on_bad_return():
    with pytest.raises(TypeError):
        f3("potato")

def test_starred():
    assert f4(1, 2) == 3
    assert f4(4, 6, 9, 12) == 31

def test_starred_fail_on_bad_arg():
    with pytest.raises(TypeError):
        f4(1, 2, "sausage")

def test_kwargs():
    assert f5(1, 2, subtract=True) == -1
    assert f5(7, 2, multiply=True) == 14

    with pytest.raises(TypeError):
        f5(1, 2, subtract=99)

def test_nonetype():
    f6(3)
    assert f7() == 0