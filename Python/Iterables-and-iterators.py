from itertools import combinations, starmap

_ = int(input())

it = list(
    starmap(lambda *x: "a" in x, combinations("".join(input().split()), int(input())))
)

print(sum(it) / len(it))
