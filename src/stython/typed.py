from typing import Optional
from warnings import warn

from stython.checker import _isinstance

class Typed:
    """Transparent wrapper class for statically typed variables. Ensures that variable type cannot be changed after
    declaration. Ideally, this would be created by a preprocessor that can convert type annotations into Typed
    classes."""
    _typeof = None
    value = None

    def __init__(self, value: any, typeof: Optional[type] = None):
        if typeof is not None:
            self._typeof = typeof
            if not _isinstance(value, typeof):
                raise TypeError(f"Assignment of typed variable: Expected {typeof}, got {type(value)}")
        self.value = value
        if typeof is None:
            self._typeof = type(value)
            warn(
                f"Typed variable assigned implicitly to {self._typeof}. Consider explicitly defining an expected type.",
                stacklevel=2
            )

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value: any):
        if not _isinstance(value, self._typeof):
            raise TypeError(f"Reassignment of typed variable: Expected {self._typeof}, got {type(value)}")
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)