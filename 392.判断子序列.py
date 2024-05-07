#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    """
    双指针，定义两个指针分别指向s和t的开头，然后逐个比较字符
    如果相等，则s指针后移，否则t指针后移
    最后判断s指针是否到达s的末尾 
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)
# @lc code=end

