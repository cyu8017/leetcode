# LeetCode 0623 - Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/

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
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def dfs(node: Optional[TreeNode], current: int) -> None:
            if not node:
                return
            if current == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, current + 1)
            dfs(node.right, current + 1)

        dfs(root, 1)
        return root
