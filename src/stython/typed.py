

class Typed:
    """Transparent wrapper class for statically typed variables. Ensures that variable type cannot be changed after
    declaration. Ideally, this would be created by a preprocessor that can convert type annotations into Typed
    classes."""
    _typeof = None
    value = None

    def __init__(self, value, typeof):
        self._typeof = typeof
        if not isinstance(value, typeof):
            raise TypeError(f"Expected {typeof}, got {type(value)}")
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, self._typeof):
            raise TypeError(f"Expected {self._typeof}, got {type(value)}")
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)