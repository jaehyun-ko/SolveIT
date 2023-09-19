def solution(arr):
    answer = [arr[0]]
    for data in arr:
        if answer[-1]==data:
            continue
        answer.append(data)
    return answer