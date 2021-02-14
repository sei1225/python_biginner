animal = 'cat'


def f():
    global animal
    animal = 'dog'
    print("local:", animal)


f()
print("global:", animal)
