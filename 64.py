"""
TEST Test
"""

animal = "cat"


def f():
    """
    this is f's description
    """
    # global animal
    # animal = "dog"
    # print("local:", locals())
    print(f.__name__)
    print(f.__doc__)


f()
# print("global:", globals())
print("global:", __name__)
