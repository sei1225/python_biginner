def say_something():
    s = "hi"
    return s


result = say_something()
print(result)


def what_is_this(color):
    if(color == "red"):
        return "tomato"
    elif(color == "green"):
        return "green papper"
    else:
        return "I don't know"


result_1 = what_is_this("red")
result_2 = what_is_this("green")
result_3 = what_is_this("blue")

print(result_1)
print(result_2)
print(result_3)
