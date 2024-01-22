from itertools import permutations

def solution(k, dungeons):
    result_list=[]
    ktemp=k
    for dungeon_list in permutations(dungeons):
        # print(dungeon_list)
        k =  ktemp
        result = -1
        for dungeon in dungeon_list:
            # print(dungeon)
            if dungeon[0]<=k and k-dungeon[1]>=0:
                result+=1
                k-=dungeon[1]
                # print(f'k: {k}')
            else:
                break
        result_list.append(result+1)
        # print(result_list)
    answer = max(result_list)
    # print(f'result_list: {result_list}')
    return answer