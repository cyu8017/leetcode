# LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

from typing import Optional, Tuple


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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal best
            if not node:
                return 0, 0

            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)

            inc = dec = 1
            if node.left:
                if node.left.val == node.val + 1:
                    inc = max(inc, left_inc + 1)
                elif node.left.val == node.val - 1:
                    dec = max(dec, left_dec + 1)
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.right.val == node.val - 1:
                    dec = max(dec, right_dec + 1)

            if node.left and node.right:
                if node.left.val + 1 == node.val == node.right.val - 1:
                    best = max(best, left_dec + 1 + right_inc)
                if node.left.val - 1 == node.val == node.right.val + 1:
                    best = max(best, left_inc + 1 + right_dec)

            best = max(best, inc, dec)
            return inc, dec

        dfs(root)
        return best
