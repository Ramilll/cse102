def transacts_num(n):
    transactions = [1, 3, 7, 9]
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in transactions:
            if i >= j:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[n]


def transacts_list(n):
    dp = [0 for _ in range(n + 1)]
    prev = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in [1, 3, 7, 9]:
            if i >= j and (dp[i - j] + 1 < dp[i] or dp[i] == 0):
                dp[i] = dp[i - j] + 1
                prev[i][dp[i]] = j

    result = []
    i = n
    j = dp[n]
    while i > 0:
        result.append(prev[i][j])
        i -= prev[i][j]
        j -= 1

    return result
