tu = (1, 2, 3, 4, 5)
tu2 = (6, 7, 8, 9, 10)

# r = []

# for i in tu:
#     if i % 2 == 0:
#         r.append(i)


r = [i for i in tu if i % 2 == 0]

print(r)

# ↓こういう書き方もできるが、この場合は可読性が悪いので実際の開発では非推奨となる
r = [i*j for i in tu for j in tu2]
print(r)
