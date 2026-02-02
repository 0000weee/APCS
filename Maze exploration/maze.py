import sys
sys.setrecursionlimit(10**6)  # 避免遞迴深度不夠

# ========================
# 1. 讀入紀錄
# ========================
record = list(map(int, input().split()))
n = len(record)
total = 0  # 累加父子編號差絕對值總和

# ========================
# 2. 遞迴處理
# ========================
def dfs(i):
    """
    遞迴遍歷樹狀迷宮
    i: 當前索引
    返回值: 遍歷完當前節點後的索引
    """
    global total
    cur = record[i]
    i += 1

    # 判斷出口數量
    if cur % 2 == 0:
        num_children = 2
    else:
        num_children = 3

    # 處理每個出口
    for _ in range(num_children):
        if i >= n:
            break  # 防止超出範圍
        child = record[i]
        if child == 0:
            # 死路
            i += 1
        else:
            # 計算父子差值
            total += abs(cur - child)
            # 遞迴探索子節點
            i = dfs(i)
    return i

# ========================
# 3. 呼叫 dfs 處理整個迷宮
# ========================
dfs(0)

# ========================
# 4. 輸出結果
# ========================
print(total)
