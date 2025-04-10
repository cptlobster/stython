import functools
import inspect
from types import NoneType

from stython import STYTHON_REQUIRE_ANNOTATIONS

def typecheck(f):
    """Dynamically check type annotations for a class, function, method, or other types.

    :raises AttributeError: if a type annotation is missing and `STYTHON_REQUIRE_ANNOTATIONS` is set
    :raises TypeError: in case of a type mismatch."""
    if inspect.isfunction(f):
        return typecheck_function(f)
    if inspect.ismethod(f):
        return typecheck_function(f)

def typecheck_function(f):
    """Dynamically check a function's type annotations to ensure that input arguments and return types match actual
    values.

    :raises AttributeError: if a type annotation is missing and `STYTHON_REQUIRE_ANNOTATIONS` is set
    :raises TypeError: in case of a type mismatch."""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # TODO: parse function arguments and check types; need to handle starred arguments properly
        result = f(*args, **kwargs)
        fail_if_invalid(f, "return", result)
        return result
    return wrapper

def check(f, k, v) -> bool:
    """Check if a variable matches a type annotation. If `STYTHON_REQUIRE_ANNOTATIONS` is set, missing type annotations
    will throw an error.

    :param f: The function to check the signature of.
    :param k: The parameter name.
    :param v: The value of the parameter.

    :returns: True if the signature matches, False otherwise.

    :raises AttributeError: if a type annotation is missing and `STYTHON_REQUIRE_ANNOTATIONS` is set"""
    if k in f.__annotations__:
        return isinstance(v, f.__annotations__[k])
    else:
        if not isinstance(v, NoneType) and STYTHON_REQUIRE_ANNOTATIONS:
            raise AttributeError(f"no type annotation found for {k}")
        else:
            return True

def fail_if_invalid(f, k, v):
    """Fail if a type does not match.

    :param f: The function to check the signature of.
    :param k: The parameter name.
    :param v: The value of the parameter.

    :returns: True if the signature matches, False otherwise.

    :raises AttributeError: if a type annotation is missing and `STYTHON_REQUIRE_ANNOTATIONS` is set
    :raises TypeError: in case of a type mismatch."""
    if not check(f, k, v):
        if k == "return":
            raise TypeError(f"Expected to return {f.__annotations__.get(k)}, got {type(v)}")
        raise TypeError(f"{k}: Expected {f.__annotations__.get(k)}, got {type(v)}")