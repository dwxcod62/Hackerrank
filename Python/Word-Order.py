n = int(input())

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


word_counter = OrderedCounter([input() for _ in range(n)])

print(len(word_counter))
print(*[item[1] for item in word_counter.items()])
