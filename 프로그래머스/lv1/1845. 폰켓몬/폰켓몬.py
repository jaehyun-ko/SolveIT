def solution(nums):
    # N = len(nums)
    # n = N/2
    # k = len(set(nums))
    # if k > n:
    #     answer = n
    # else:
    #     answer = k
    return min(len(nums)/2, len(set(nums)))