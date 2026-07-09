import time

# 品物データ
# (価値, 重さ)
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

# 品物数
n = len(items)

# DP表を0で初期化
# dp[i][w] = 最初のi個で容量wのときの最大価値
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# 処理時間の計測開始
start = time.perf_counter()

# DP表を上から順番に埋める
for i in range(1, n + 1):

    # 現在見ている品物
    value, weight = items[i - 1]

    # 容量を0～45まで順番に調べる
    for w in range(capacity + 1):

        # 品物が入らない場合
        if weight > w:
            dp[i][w] = dp[i - 1][w]

        # 品物が入る場合
        else:
            dp[i][w] = max(
                dp[i - 1][w],                  # 入れない
                dp[i - 1][w - weight] + value  # 入れる
            )

# 処理時間の計測終了
end = time.perf_counter()

# -----------------------------
# 選ばれた品物を逆向きに復元する
# -----------------------------

selected = []

w = capacity

# DP表を最後からたどる
for i in range(n, 0, -1):

    # 上の値と違えば、この品物を選んだことになる
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= items[i - 1][1]

# 番号順に並べる
selected.reverse()

print("選択した品物:", selected)
print("最大価値:", dp[n][capacity])
print("処理時間:", end - start, "秒")