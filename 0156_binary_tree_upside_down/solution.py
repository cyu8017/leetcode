# LeetCode 0156 - Binary Tree Upside Down
# https://leetcode.com/problems/binary-tree-upside-down/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = None
        prev_right = None
        current = root
        while current:
            nxt = current.left
            current.left = prev_right
            prev_right = current.right
            current.right = prev
            prev = current
            current = nxt
        return prev
