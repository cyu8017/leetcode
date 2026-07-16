# LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> tuple[TreeNode, int]:
            if not node:
                return None, 0
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_node, left_depth + 1
            if right_depth > left_depth:
                return right_node, right_depth + 1
            return node, left_depth + 1

        return dfs(root)[0]
