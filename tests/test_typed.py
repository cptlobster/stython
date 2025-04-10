import pytest
from stython.typed import Typed

def test_typed():
    v0 = Typed("hello", str)
    v1 = Typed(4, int)

    assert v1 == 4
    assert v0 == "hello"

    assert str(v1) == "4"