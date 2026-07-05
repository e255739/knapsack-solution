items = [
    (6, 4),
    (12, 8),
    (4, 3),
    (3, 5),
    (7, 9),
    (1, 2),
    (3, 3),
    (2, 1),
    (7, 5),
    (3, 2),
    (4, 4),
    (2, 2),
    (10, 7),
    (13, 10),
    (5, 3),
    (16, 13),
    (14, 11),
    (9, 8)
]

capacity = 45

n = len(items)

dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    value, weight = items[i - 1]

    for w in range(capacity + 1):

        if weight > w:
            dp[i][w] = dp[i - 1][w]

        else:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - weight] + value
            )

print(dp[n][capacity])