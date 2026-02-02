nums = list(map(int, input().split()))

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
def print_dfs(u):
    if u == -1:
        return

    # 印自己
    print(node_value[u], end='')

    # 印左子節點（若存在）
    if left_child[u] != -1:
        print(' ' + str(node_value[left_child[u]]), end='')

    # 印右子節點（若存在）
    if right_child[u] != -1:
        print(' ' + str(node_value[right_child[u]]), end='')

    # 節點結尾
    print(',', end='')

    # DFS
    print_dfs(left_child[u])
    print_dfs(right_child[u])

root = dfs()
print_dfs(root)
print()  # 換行
