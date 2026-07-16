# LeetCode 1110 - Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        delete = set(to_delete)
        forest: list[TreeNode] = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            removed = node.val in delete
            if is_root and not removed:
                forest.append(node)
            node.left = dfs(node.left, removed)
            node.right = dfs(node.right, removed)
            return None if removed else node

        dfs(root, True)
        return forest
