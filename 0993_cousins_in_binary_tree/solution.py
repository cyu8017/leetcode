# LeetCode 0993 - Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info: dict[int, tuple[int, Optional[TreeNode]]] = {}

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if node.val in (x, y):
                info[node.val] = (depth, parent)
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        return info[x][0] == info[y][0] and info[x][1] is not info[y][1]
