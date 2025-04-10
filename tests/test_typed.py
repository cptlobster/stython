import pytest
from stython.typed import Typed

def test_typed():
    v0 = Typed("hello")
    v1 = Typed(4)

    assert v1 == 4
    assert v0 == "hello"

    assert str(v1) == "4"

def test_typed_assign_fail():
    with pytest.raises(TypeError):
        Typed("hello", int)

def test_typed_reassign_fail():
    with pytest.raises(TypeError):
        v0 = Typed("hello")
        v0 = 4
