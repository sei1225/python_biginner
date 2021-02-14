r = [1, 2, 3, 4, 5, 1, 2, 3]
result = r.index(2, 2)
print(result)
result = r.count(2)
print(result)

if 5 in r:
    print("exist")

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = "My name is Mike"
result = s.split(" ")
print(result)

x = " ".join(result)
print(x, end=".")

print(help(list))
