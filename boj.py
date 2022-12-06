# 1003. 피보나치 함수
dp = [(1, 0), (0, 1)] # dp[i] = i번째 수의 (0 출력 횟수, 1 출력 횟수)

'''
피보나치 수열의 점화식과 같은 원리로 동작함
따라서 피보나치 수열을 구하는 것과 같은 방식으로 구현
N의 제한이 40밖에 안되므로 미리 재귀로 구해두고 출력하면 된다.
'''
def fibo_cnt(n, dp):
    for i in range(2, n+1):
        dp.append((dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]))
    return dp


dp = fibo_cnt(40, dp)

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])