#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    """
    方法1：哈希表 直接统计字符出现次数 如：Map<String, int>
    因为str只包括小写字母
    可以Ascii码值减去'a'的Ascii码值，得到一个0-25的值，作为数组的下标表示a-z
    然后遍历magazine，统计每个字符出现的次数
    遍历ransomNote，减去magazine中相应字符的次数，如果出现负数，则返回False
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        cnt = [0] * 26
        for i in magazine:
            cnt[ord(i) - ord('a')] += 1  
        for i in ransomNote:
            cnt[ord(i) - ord('a')] -= 1
            if cnt[ord(i) - ord('a')] < 0:
                return False
        return True
# @lc code=end

