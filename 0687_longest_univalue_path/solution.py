# LeetCode 0687 - Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0
            best = max(best, left_path + right_path)
            return max(left_path, right_path)

        dfs(root)
        return best
