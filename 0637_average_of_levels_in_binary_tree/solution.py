# LeetCode 0637 - Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result: list[float] = []
        queue: deque[TreeNode] = deque([root])
        while queue:
            total = 0
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(total / count)
        return result
