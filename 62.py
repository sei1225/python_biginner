s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)


print(s)


s = {i for i in range(10) if i % 2 == 0}
print(s)
