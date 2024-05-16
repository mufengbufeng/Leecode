#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num < 0: num = (1 << 32) + num   
        if num == 0: return '0'
        hex_chars = '0123456789abcdef' 
        res = ''
        while num > 0:
            digit = num % 16 
            res = hex_chars[digit] + res 
            num = (num - digit) // 16
        return res
    

# @lc code=end

