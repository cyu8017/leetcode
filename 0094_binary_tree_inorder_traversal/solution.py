# LeetCode 0094 - Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
