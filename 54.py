def example_func(param1: int, param2: str) -> bool:
    """

    Args:param1(int):The first parameter
    Args:param2(str):The second parameter

    Returns:
        bool:The return value.True for success.False otherwise.

    """
    print(param1)
    print(param2)
    return True


# print(example_func.__doc__)
help(example_func)

#htmlに記述したりするときに使える
