

def _isinstance(value: any, typeof: type) -> bool:
    """check if the value matches the type signature given by typeof."""
    # TODO: subscripted generics cannot be used with class and instance checks
    return isinstance(value, typeof)