#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, isLeft):
        if not node: return 0
        if not node.left and not node.right and isLeft:
            return node.val
        return self.dfs(node.left, True) + self.dfs(node.right, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, False)



