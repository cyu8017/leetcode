# LeetCode 1022 - Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], value: int) -> int:
            if not node:
                return 0
            value = value * 2 + node.val
            if not node.left and not node.right:
                return value
            return dfs(node.left, value) + dfs(node.right, value)

        return dfs(root, 0)
