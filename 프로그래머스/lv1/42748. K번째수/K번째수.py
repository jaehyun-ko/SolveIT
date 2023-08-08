def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        print(array[i-1:j])
        data = sorted(array[i-1:j])[k-1]
        answer.append(data)
    return answer