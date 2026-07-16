# LeetCode 0222 - Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_depth(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        def right_depth(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth

        left = left_depth(root)
        right = right_depth(root)
        if left == right:
            return (1 << left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
