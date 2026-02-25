def cal(s):  # 計算
    temp = s.split('*')
    arr = []
    for i in temp:
        i = i.split('+')
        total = 0
        for j in i:
            total += int(j)
        arr.append(total)
    ans = 1
    for i in arr:
        ans *= int(i)
    return ans

def find_right(s, start): # 回傳右括號的位置
    count = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1  # 沒找到

def calculate_f(s, start, end):
    # 我們取括號內的內容
    content = s[start+1:end] 
    
    resolved_content = ""
    idx = 0
    while idx < len(content):
        if content[idx] == 'f':
            f_start_idx = idx + 1 # '('
            f_end_idx = find_right(content, f_start_idx)
            f_val = calculate_f(content, f_start_idx, f_end_idx)
            resolved_content += str(f_val)
            idx = f_end_idx + 1
        else:
            resolved_content += content[idx]
            idx += 1
    
    params = resolved_content.split(',')
    nums = []
    for p in params:
        if p.strip(): # 確保參數不是空的
            nums.append(cal(p))
    
    if not nums: return 0
    return max(nums) - min(nums)



# main()

s = input()

buf = ""

i = 0
while (i < len(s)):
    if (s[i] != 'f'):
        buf += s[i]
        i += 1
    else:
        start = i + 1
        end = find_right(s, start)
        f_value = calculate_f(s, start, end)
        buf += str(f_value)
        i = end + 1

print(cal(buf))