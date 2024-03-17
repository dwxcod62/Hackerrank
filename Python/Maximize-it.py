rows, modus = map(int, input().split())
matrix = [tuple(set(map(int, input().split()[1:]))) for _ in range(rows)]
sq = lambda x: x**2
pair_wise = [[]]

max_value = sum(map(sq, map(max, matrix)))

if max_value < modus:
    print(max_value % modus)
else:
    for tups in matrix:
        pair_wise = [braces + [sq(items)] for braces in pair_wise for items in tups]
    pair_wise = [sum(item) % modus for item in pair_wise]
    max_value = max(pair_wise)
    print(max_value)
