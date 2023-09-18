
def dup_test(words:list):
    check = {}
    for idx, word in enumerate(words):
        try:
            check[word]
            return idx
        except:
            check[word] = 1
    return 0
        
def crash_test(words:list):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return i+1
    return 0

def solution(n, words):
    t = max(dup_test(words), crash_test(words)) if not dup_test(words) * crash_test(words) else min(dup_test(words), crash_test(words))
    print(t)
    if t > 0:
        return [t%n+1, t//n+1]
    return [0, 0]