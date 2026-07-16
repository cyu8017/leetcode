# LeetCode 0662 - Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque
from typing import Optional


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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
        best = 0
        while queue:
            left = queue[0][1]
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                best = max(best, idx - left + 1)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
        return best
