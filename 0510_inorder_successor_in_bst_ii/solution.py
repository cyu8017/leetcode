# LeetCode 0510 - Inorder Successor in BST II
# https://leetcode.com/problems/inorder-successor-in-bst-ii/

from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        parent: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def inorderSuccessor(self, node: Node) -> Optional[Node]:
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        current = node
        while current.parent and current is current.parent.right:
            current = current.parent
        return current.parent
