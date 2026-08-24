# LeetCode 2689 - Extract Kth Character From The Rope Tree
# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

from typing import Optional


class RopeTreeNode:
    def __init__(self, len: int = 0, val: str = "", left=None, right=None):
        self.len = len
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getKthCharacter(self, root: Optional[RopeTreeNode], k: int) -> str:
        def dfs(node: RopeTreeNode, kk: int) -> str:
            if not node.left and not node.right:
                return node.val
            left_len = 0
            if node.left:
                left_len = node.left.len if node.left.len > 0 else 1
            if kk <= left_len:
                return dfs(node.left, kk)
            return dfs(node.right, kk - left_len)

        return dfs(root, k)
