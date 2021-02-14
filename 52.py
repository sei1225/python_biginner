def say_something(word, *args):
    print("word = ", word)
    for arg in args:
        print(arg)


say_something("Hi!", "Mike", "Nancy")

# t = ("Mike", "Nancy")
# say_something("Hi!", *t)
