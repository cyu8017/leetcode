# LeetCode 0538 - Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    def convertBST(self, root: Optional[TreeNode]) -> None:
        running = 0

        def reverse_inorder(node: Optional[TreeNode]) -> None:
            nonlocal running
            if not node:
                return
            reverse_inorder(node.right)
            running += node.val
            node.val = running
            reverse_inorder(node.left)

        reverse_inorder(root)
