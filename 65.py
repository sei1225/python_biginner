li = [1, 2, 3]
i = 5
# del li

try:
    li[0]
except IndexError as exc:
    print(f"Don't worry:{exc}")
except NameError as exc:
    print(f"Don't worry:{exc}")
except BaseException as exc:
    # すべてのExceptionをキャッチするというような実装は業務的にはよくないよ
    print(f"other:{exc}")
else:
    print("done")
finally:
    print("clean up")
