def outer(a: int, b: int) -> int:
    def inner(c: int, d: int) -> int:
        return c + b

    r1 = inner(a, b) 
    r2 = inner(r1, b)
    return r1 + r2


print(outer(1, 2))
