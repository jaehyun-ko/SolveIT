def count(answers):
    p = [
        [i for i in range(1,6)]*2000,
         [2, 1, 2, 3, 2, 4, 2, 5]*2000,
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*2000
         ]
    cnt_list = [0 for i in range(3)]
    for i, answer in enumerate(answers):
        for j, cnt in enumerate(cnt_list):
            # print(answer, p[j][i])
            if answer==p[j][i]:
                cnt_list[j] += 1    
            # print(cnt)
    return cnt_list

def solution(answers):
    cnt_list = count(answers)
    max_cnt = max(cnt_list)
    answer = []
    for i, cnt in enumerate(cnt_list):
        if cnt == max_cnt:
            answer.append(i+1)
    return answer
