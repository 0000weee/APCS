```
EvaluatePrefix (expression) ：
    初始化 stack 為空的堆疊
    從右到左遍歷 expression：
    If 當前元素是數字：
    將數字壓入 stack
    If 當前元素是運算符 (+, -, *, /)：
    彈出 stack 頂端的兩個數字 num1、num2
    計算 (num1 運算符 num2)
    將計算結果壓回 stack
    return stack 最後剩下的數值
 ```