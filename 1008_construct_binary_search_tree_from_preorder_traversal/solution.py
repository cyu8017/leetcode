# LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        self.i = 0

        def build(bound: float) -> Optional[TreeNode]:
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root

        return build(float("inf"))
