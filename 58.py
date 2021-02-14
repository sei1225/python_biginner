li = ["Mon", "tue", "Wed", "thr", "fri", "Sat", "sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word: str) -> str:
#     return word.capitalize()


change_words(li, lambda word: word.capitalize())
change_words(li, lambda word: word.lower())

# functionを引数として呼び出す関数で効果的
