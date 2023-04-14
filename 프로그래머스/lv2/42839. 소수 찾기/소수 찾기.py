import math
from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int(math.sqrt(number))+1):
        if number%num == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    number_set = set()
    for i in range(1, len(numbers)+1):
        number_set.update(map(int, map("".join, list(permutations(numbers, i)))))
    return sum(map(is_prime, number_set))