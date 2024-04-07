#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (49.33%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    260.7K
# Total Submissions: 528.5K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 
# 
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：s = "egg", t = "add"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "foo", t = "bar"
# 输出：false
# 
# 示例 3：
# 
# 
# 输入：s = "paper", t = "title"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
# 
# 
#

# @lc code=start
class Solution:
    """
    用两个哈希表分别记录s到t和t到s的映射关系，如果出现了不一致的映射关系则返回False
    示例：
        first: len(s) != len(t) -> False
        egg -> add
        s2t = {}
        t2s = {} 
        遍历 egg or add:
            如果在s2t中找到了映射关系，但是映射关系不一致，返回False
            如果在t2s中找到了映射关系，但是映射关系不一致，返回False
            否则，建立映射关系
            人话：其实就是在s和t之间建立一一对应的关系，如果出现了不一致的情况，就返回False
        模拟运行:
        egg -> adg
        s2t = {}
        s2t = {}
        for a,v in zip(s, t):
            first: s2t = {'e': 'a'} t2s = {'a': 'e'}
            second: s2t不存在g t2s中不存在d s2t = {'e': 'a', 'g': 'd'} t2s = {'a': 'e', 'd': 'g'}
            third: s2t存在g对应为d v!=d 返回False 
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t: dict = {}
        t2s: dict = {}
        for a,v in zip(s, t):
            if (a in s2t and s2t[a] != v) or (v in t2s and t2s[v] != a):
                return False
            s2t[a] = v
            t2s[v] = a
        return True

# @lc code=end

