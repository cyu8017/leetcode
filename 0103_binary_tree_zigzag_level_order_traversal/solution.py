# LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])
        left_to_right = True

        while queue:
            level: List[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right

        return result
