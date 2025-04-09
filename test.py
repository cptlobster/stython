from decorators import typecheck

@typecheck
def f1(a: int, b: int) -> int:
    return a + b

@typecheck
def f2(a: str) -> int:
    return len(a)

@typecheck
def f3(a: str) -> int:
    return a

@typecheck
def f4(*a: int) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum

print(f1(1, 1))
print(f2("hello"))

try:
    print(f1(2, "beans"))
except TypeError as e:
    print(e)
    print("Task failed successfully")

try:
    print(f3("potato"))
except TypeError as e:
    print(e)
    print("Task failed successfully")

print(f4(1, 2))
print(f4(4, 6, 9, 12))