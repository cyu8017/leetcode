# LeetCode 0968 - Binary Tree Cameras
# https://leetcode.com/problems/binary-tree-cameras/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal cameras
            if node is None:
                return 1
            left, right = dfs(node.left), dfs(node.right)
            if left == 0 or right == 0:
                cameras += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0

        root_state = dfs(root)
        return cameras + (1 if root_state == 0 else 0)
