def g():
    for i in range(10):
        yield i

# g = g()
# print(next(g))


r = (i for i in range(10))
print(next(r))
print(next(r))
print(next(r))

r = tuple(i for i in range(10))
print(r)
