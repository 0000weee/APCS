# Pesudo code #
```
函式 dfs(i):
    # i 是當前 index
    cur = record[i]
    i += 1
    # 根據 cur 的奇偶判斷出口數
    if cur % 2 == 0:
        num_children = 2
    else:
        num_children = 3

    for c in 0 .. num_children-1:
        if record[i] == 0:
            # 死路，跳過
            i += 1
        else:
            # 計算差值
            total += abs(cur - record[i])
            # 遞迴
            i = dfs(i)
    return i

```

# 開發流程 #

# 劃分工作階段 #

1. 讀入資料  

2. 遞迴 DFS 重建樹  

3. 計算父子差值  

4. 輸出結果  

# 先 pseudo code，再轉 Python #

Pseudo code → 先把 DFS 結構寫下，再加入差值計算  