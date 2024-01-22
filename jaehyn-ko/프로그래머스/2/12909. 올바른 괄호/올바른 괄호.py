from collections import deque

def solution(s):
    """
    bra를 하나씩 push 하다가
    ket을 만나면 pop
    """
    bra = []
    for bin in s:
        if bin is "(":
            bra.append("(")
        else:
            try:
                bra.pop()
            except:
                return False
    if bra:
        return False
    return True