```
find_smallest_index(arr, left, right, t):
 // 若超出範圍則返回 -1
 if left > right:
 return -1
 pivot = (left + right)/ 2
 // 找到 arr[pivot] > t，且 arr[pivot-1] <= t
 if arr[pivot] > t and (pivot == 0 or arr[pivot - 1] <= t):
 return pivot
 // 若 arr[pivot] > t，往左邊搜尋
 if arr[pivot] > t:
 return find_smallest_index(arr, left, pivot - 1, t)
 // 若 arr[pivot] <= t，往右邊搜尋
 return find_smallest_index(arr, pivot + 1, right, t)
 ```
如果找不到arr[k]>t，代表t比陣列裡面最大的還要大，檢查需取得arr[n-1]的值花費 O(1)
執行一次find_smallest_index函數需要做if判斷，if判斷要檢查pivot的值，沒成功找到就
檢查pivot右半或左半
最糟糕的情況需做ln(n)次跳到左半或是右半的動作，花費 ln(n)