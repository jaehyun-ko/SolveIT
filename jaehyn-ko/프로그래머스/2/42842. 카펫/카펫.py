from math import sqrt

def factorize(n):
    factors = []
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            factors.append([int(n/i), i])
    return factors
    
def solution(brown, yellow):
    factors = factorize(brown+yellow)
    for factor in factors:
        if (factor[0]-2)*(factor[1]-2)==yellow and (factor[0]+factor[1]-2)*2==brown:
            return factor