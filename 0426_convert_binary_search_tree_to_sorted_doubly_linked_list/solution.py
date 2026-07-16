# LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        first: TreeNode | None = None
        last: TreeNode | None = None

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal first, last
            if node is None:
                return
            inorder(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            inorder(node.right)

        inorder(root)
        if first and last:
            first.left = last
            last.right = first
        return first
