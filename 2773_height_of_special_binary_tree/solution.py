# LeetCode 2773 - Height of Special Binary Tree
# https://leetcode.com/problems/height-of-special-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.left and node.left.right is node:
                return dfs(node.right) + 1
            if node.right and node.right.left is node:
                return dfs(node.left) + 1
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
