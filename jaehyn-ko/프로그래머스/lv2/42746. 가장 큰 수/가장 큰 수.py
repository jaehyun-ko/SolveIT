def solution(numbers):
    answer = ''.join(map(str, sorted(numbers, key=lambda x:str(x).ljust(4, "0"), reverse=True)))
    return answer