# LeetCode 0872 - Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return leaves(node.left) + leaves(node.right)

        return leaves(root1) == leaves(root2)
