# LeetCode 0250 - Count Univalue Subtrees
# https://leetcode.com/problems/count-univalue-subtrees/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal count
            if not node:
                return True
            left_ok = dfs(node.left)
            right_ok = dfs(node.right)
            if not left_ok or not right_ok:
                return False
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            count += 1
            return True

        dfs(root)
        return count
