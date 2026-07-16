# LeetCode 0513 - Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmost = root.val if root else 0
        while queue:
            level_size = len(queue)
            for index in range(level_size):
                node = queue.popleft()
                if index == 0:
                    leftmost = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftmost
