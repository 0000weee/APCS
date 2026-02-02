nums = list(map(int, input().strip()))

node_value  = []
left_child  = []
right_child = []

n = len(nums)
i = 0

def dfs():
    global i

    if i >= n:
        return -1

    cur = nums[i]
    i += 1

    if cur == 0:
        return -1

    # 建立當前節點
    idx = len(node_value)
    node_value.append(cur)
    left_child.append(-1)
    right_child.append(-1)

    # 建立左右子樹
    left = dfs()
    right = dfs()

    left_child[idx] = left
    right_child[idx] = right

    return idx


# 建樹
root = dfs()

print("node_value :", node_value)
print("left_child :", left_child)
print("right_child:", right_child)
print("root index :", root)
