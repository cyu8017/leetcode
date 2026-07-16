# LeetCode 0655 - Print Binary Tree
# https://leetcode.com/problems/print-binary-tree/

from typing import List, Optional


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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        rows = h + 1
        cols = (1 << (h + 1)) - 1
        res = [[""] * cols for _ in range(rows)]

        def place(node: Optional[TreeNode], r: int, c: int) -> None:
            if not node:
                return
            res[r][c] = str(node.val)
            if r == h:
                return
            offset = 1 << (h - r - 1)
            place(node.left, r + 1, c - offset)
            place(node.right, r + 1, c + offset)

        place(root, 0, (cols - 1) // 2)
        return res
