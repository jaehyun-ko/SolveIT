def solution(number, k):
    temp = [number[0]]
    for i in number[1:]:
        while len(temp)>0 and temp[-1]<i and k>0 :
            k -= 1
            temp.pop()
        temp.append(i)

    if k!= 0:
        temp = temp[:-k]
    return  ''.join(temp)