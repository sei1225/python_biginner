# li = ["GoodMorning", "GoodAfternoon", "GoodNight"]

# for i in li:
#     print(i)
# print("################################")


def counter(num=10):
    for _ in range(num):
        yield "run"


def greeting():
    yield "GoodMorning"
    yield "GoodAfternoon"
    yield "GoodNight"


# for g in greeting():
    # print(g)

c = counter()
g = greeting()


print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
