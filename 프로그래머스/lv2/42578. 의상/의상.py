from itertools import combinations
from math import prod
def solution(clothes):
    wearables = {}
    for value, key in clothes:
        try:
            wearables[key].append(value)
        except:
            wearables[key] = [value]
    tmp = [len(x)+1 for x in wearables.values()]
#    tmp = Counter([kind for name, kind in clothes])
    cnt = prod(tmp) - 1
    return cnt