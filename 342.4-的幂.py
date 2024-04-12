#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    """
     同326 三次幂
    """  
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1 and n % 4 == 0:
            n /= 4
        return n == 1
       
# @lc code=end

