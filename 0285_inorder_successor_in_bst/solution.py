# LeetCode 0285 - Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(
        self, root: TreeNode, p: TreeNode
    ) -> Optional[TreeNode]:
        if p.right:
            current = p.right
            while current.left:
                current = current.left
            return current
        successor = None
        current = root
        while current:
            if p.val < current.val:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor
