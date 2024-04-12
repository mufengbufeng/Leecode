#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    """
    hash表统计字符出现次数
    """

    def firstUniqChar(self, s: str) -> int:
        sMap = {}
        for i in s:
            sMap[i] = sMap.get(i, 0) + 1
        for i in range(len(s)):
            if sMap[s[i]] == 1:
                return i 
        return -1
# @lc code=end

