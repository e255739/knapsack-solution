import time

# 品物データ
# [品物番号, 重さ, 価値]
items = [
    [1, 4, 6],
    [2, 8, 12],
    [3, 3, 4],
    [4, 5, 3],
    [5, 9, 7],
    [6, 2, 1],
    [7, 3, 3],
    [8, 1, 2],
    [9, 5, 7],
    [10, 2, 3],
    [11, 4, 4],
    [12, 2, 2],
    [13, 7, 10],
    [14, 10, 13],
    [15, 3, 5],
    [16, 13, 16],
    [17, 11, 14],
    [18, 8, 9]
]

# ナップサックの容量
capacity = 45

# 現在の最適解を保存する変数
best_value = 0
best_weight = 0
best_choice = []

# 処理時間の計測開始
start = time.perf_counter()

# 全ての組み合わせを試す（2^18通り）
for x in range(2 ** len(items)):

    # xを0と1の選択配列へ変換
    # 例：1010 → [0,1,0,1]
    choice = []
    for i in range(len(items)):
        choice.append((x >> i) & 1)

    # この組み合わせの重さと価値を計算する
    total_weight = 0
    total_value = 0

    for i in range(len(items)):
        if choice[i] == 1:
            total_weight += items[i][1]
            total_value += items[i][2]

    # 容量以内で、これまでより価値が大きければ更新
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_weight = total_weight
        best_choice = choice.copy()

# 処理時間の計測終了
end = time.perf_counter()

# 選ばれた品物番号を表示用に取り出す
selected = []
for i in range(len(best_choice)):
    if best_choice[i] == 1:
        selected.append(items[i][0])

print("選択した品物:", selected)
print("最大価値:", best_value)
print("重さ:", best_weight)
print("処理時間:", end - start, "秒")