# LeetCode 2641 - Cousins in Binary Tree II
# https://leetcode.com/problems/cousins-in-binary-tree-ii/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.val = 0
        q = deque([root])
        while q:
            sz = len(q)
            level_sum = 0
            level = []
            for _ in range(sz):
                node = q.popleft()
                level.append(node)
                if node.left:
                    level_sum += node.left.val
                if node.right:
                    level_sum += node.right.val
            for node in level:
                cousin = level_sum
                if node.left:
                    cousin -= node.left.val
                if node.right:
                    cousin -= node.right.val
                if node.left:
                    node.left.val = cousin
                    q.append(node.left)
                if node.right:
                    node.right.val = cousin
                    q.append(node.right)
        return root
