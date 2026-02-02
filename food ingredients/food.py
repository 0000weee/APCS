import sys

# 使用 readline 提高輸入穩定度（競賽常用）
input = sys.stdin.readline


# ========================
# 1. 讀取食物資料
# ========================

n = int(input().strip())

# foods: 食物名稱 -> 成分集合
foods = {}

for _ in range(n):
    parts = input().strip().split()

    food_name = parts[0]          # 食物名稱
    k = int(parts[1])             # 成分數量（題目給的，實際上不一定要用）
    ingredients = set(parts[2:])  # 剩下的就是成分

    foods[food_name] = ingredients


# ========================
# 2. 處理查詢
# ========================

m = int(input().strip())

for _ in range(m):
    f1, f2 = input().strip().split()

    # 邏輯計算：找交集
    common = foods[f1] & foods[f2]

    # ========================
    # 3. 輸出結果
    # ========================

    if not common:
        # 沒有共同成分
        print("nothing")
    else:
        # 依字典序輸出
        print(" ".join(sorted(common)))
