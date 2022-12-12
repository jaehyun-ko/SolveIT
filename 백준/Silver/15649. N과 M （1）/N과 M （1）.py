# 15649. n과 m (1)
'''
순열을 구하는 문제
'''

from itertools import permutations

N, M = map(int, input().split())
n = range(1, N+1)
result = list(permutations(n, M))
for data in result:
    print(*data)