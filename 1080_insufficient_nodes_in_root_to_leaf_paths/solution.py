# LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], path_sum: int) -> Optional[TreeNode]:
            if not node:
                return None
            path_sum += node.val
            if not node.left and not node.right:
                return node if path_sum >= limit else None
            node.left = dfs(node.left, path_sum)
            node.right = dfs(node.right, path_sum)
            if not node.left and not node.right:
                return None
            return node

        return dfs(root, 0)
