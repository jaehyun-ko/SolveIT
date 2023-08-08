def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        try:
            print(array[i-1:j-1])
            data = sorted(array[i-1:j])[k-1]
        except:
            data = array[i-1]
        answer.append(data)
    return answer