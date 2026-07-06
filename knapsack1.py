items = [      #test
    [1, 4, 6],   #(品物番号, 容量, 値段)
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

capacity = 45

best_value = 0
best_weight = 0
best_choice = []

for x in range(2 ** len(items)):

    # xを0/1の選択配列に変換
    choice = []
    for i in range(len(items)):
        choice.append((x >> i) & 1)

    # この組み合わせの重さ・価値を計算
    total_weight = 0
    total_value = 0

    for i in range(len(items)):
        if choice[i] == 1:
            total_weight += items[i][1]
            total_value += items[i][2]

    # 最適解を更新
    if total_weight <= capacity and total_value > best_value:
        best_value = total_value
        best_weight = total_weight
        best_choice = choice.copy()

print("最大価値:", best_value)
print("重さ:", best_weight)
print("選択:", best_choice)