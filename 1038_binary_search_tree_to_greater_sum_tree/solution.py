# LeetCode 1038 - Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def reverse_inorder(node: Optional[TreeNode]) -> None:
            nonlocal total
            if not node:
                return
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
