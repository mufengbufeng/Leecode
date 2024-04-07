#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
# https://leetcode.cn/problems/power-of-two/description/
#
# algorithms
# Easy (49.80%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    332.5K
# Total Submissions: 667.7K
# Testcase Example:  '1'
#
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 
# 如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 1
# 输出：true
# 解释：2^0 = 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 16
# 输出：true
# 解释：2^4 = 16
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# 
# 进阶：你能够不使用循环/递归解决此问题吗？
# 
#

# @lc code=start
class Solution:
    """
    first: 2的幂的二进制表示中只有一个1，其余都是0
        如： 2^0 = 0001   2^1 = 0010 2^2 = 0100 2^3 = 1000
    推论得出: 2的幂 在二进制中的运算其实就是 n << 1
    n - 1 为 n 的二进制表示中最右边的1变为0，其余不变 1000 - 1 = 0111
    如果 n 是2的幂，则 n & (n - 1) = 0
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
        # 二进制中2的幂为 10 100 1000 10000 100000
        # n - 1 为 01 011 0111 01111 011111
        # n & (n - 1) 为 0 0 0 0 0
# @lc code=end

