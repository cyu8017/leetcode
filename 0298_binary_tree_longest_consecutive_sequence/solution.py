# LeetCode 0298 - Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode], length: int) -> int:
            if node is None:
                return 0
            current = length + 1 if parent is not None and parent.val + 1 == node.val else 1
            return max(
                current,
                dfs(node.left, node, current),
                dfs(node.right, node, current),
            )

        return dfs(root, None, 0)
