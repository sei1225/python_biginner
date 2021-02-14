class UpperCaseError(Exception):
    pass


def check():
    words = ["APPLE", "orange", "banana"]
    for word in words:
        if word.isupper():
            raise UpperCaseError(word)


try:
    check()
except UpperCaseError:
    print("this is my falut. Go next")
