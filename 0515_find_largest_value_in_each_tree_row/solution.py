# LeetCode 0515 - Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        result: list[int] = []
        queue = deque([root])
        while queue:
            level_max = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result
