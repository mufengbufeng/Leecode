#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (64.18%)
# Likes:    1546
# Dislikes: 0
# Total Accepted:    496K
# Total Submissions: 772.8K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」 定义为：
# 
# 
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 
# 
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    """
    快乐数
    其实本质是链表找环问题，快慢指针
    示例：
        2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 
        19 -> 82 -> 68 -> 100 -> 1 - > 1 -> 1 -> 1 -> 1 -> 1
        假设有两个指针，一个每次走一步，一个每次走两步， 如果没有环，他们永远不会相遇
        如果有环，他们一定会在环内相遇 
        如果得到的结果是1，1^2 = 1，环的组成 就是 1 -> 1 -> 1 -> 1 -> 1 -> 1
        他们相遇的地方就是1
        如果得到的结果不是1， 那就不是快乐数
    """
    def bitSquareSum(self, n: int) -> int:
        res: int = 0
        while n > 0:
            res += (n % 10) ** 2
            n = int(n / 10)
        return res 

    def isHappy(self, n: int) -> bool:
        slow: int = n
        fast: int = n
        while True:
            slow: int = self.bitSquareSum(slow)
            fast: int = self.bitSquareSum(fast)
            fast: int = self.bitSquareSum(fast)
            print(slow, fast)
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
self = Solution()
self.isHappy(19)
# @lc code=end

