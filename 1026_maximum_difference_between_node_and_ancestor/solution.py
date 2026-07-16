# LeetCode 1026 - Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], lo: int, hi: int) -> int:
            if not node:
                return hi - lo
            lo = min(lo, node.val)
            hi = max(hi, node.val)
            return max(dfs(node.left, lo, hi), dfs(node.right, lo, hi))

        return dfs(root, root.val, root.val)
