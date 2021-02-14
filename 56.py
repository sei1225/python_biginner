# def outer(a: int, b: int) -> None:
#     def inner() -> int:
#         return a + b

#     return inner


# f = outer(1, 2)
# r = f()
# print(r)


def circle_area_func(pie: float) -> None:
    def circle_area(radius: int) -> float:
        return pie * (radius ** 2)

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159265)

print(ca1(10))
print(ca2(10))
