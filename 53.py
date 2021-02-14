def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(k, ":", v)


menu("banana", "orange", "calot", entree="salad", drink="coffee")

# d = {"entree": "salad", "drink": "coffee", "desert": "ice"}
# menu(**d)
