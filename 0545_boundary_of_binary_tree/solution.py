# LeetCode 0545 - Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/

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
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def is_leaf(node: Optional[TreeNode]) -> bool:
            return node is not None and node.left is None and node.right is None

        def left_boundary(node: Optional[TreeNode]) -> List[int]:
            if not node or is_leaf(node):
                return []
            if node.left:
                return [node.val] + left_boundary(node.left)
            return [node.val] + left_boundary(node.right)

        def right_boundary(node: Optional[TreeNode]) -> List[int]:
            if not node or is_leaf(node):
                return []
            if node.right:
                return right_boundary(node.right) + [node.val]
            return right_boundary(node.left) + [node.val]

        def leaves(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            if is_leaf(node):
                return [node.val]
            return leaves(node.left) + leaves(node.right)

        if is_leaf(root):
            return [root.val]

        return [root.val] + left_boundary(root.left) + leaves(root) + right_boundary(root.right)
