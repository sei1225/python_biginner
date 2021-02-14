# 参照渡しのものをデフォルト引数とするのはよくないよという話
# def test_func(x, li=[]):
#     li.append(x)
#     return li

# じゃあ、どうすればよいか...?
# ->None型にしてあげて、既にliが生成されている場合はliを別途生成するみたいな処理にする
def test_func(x, li=None):
    if li is None:
        li = []
    li.append(x)
    return li


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)
r = test_func(200)
print(r)
r = test_func(200)
print(r)
