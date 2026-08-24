# LeetCode 3157 - Find the Level of Tree with Minimum Sum
# https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        s = 10**18
        ans = 0
        level = 1
        while q:
            t = 0
            m = len(q)
            while m > 0:
                node = q.popleft()
                t += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                m -= 1
            if s > t:
                s = t
                ans = level
            level += 1
        return ans
