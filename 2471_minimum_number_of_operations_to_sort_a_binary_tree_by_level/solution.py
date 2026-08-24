# LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([root])
        while q:
            sz = len(q)
            vals = [0] * sz
            for i in range(sz):
                node = q.popleft()
                vals[i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sorted_vals = sorted(vals)
            pos = {vals[i]: i for i in range(sz)}
            for i in range(sz):
                if vals[i] != sorted_vals[i]:
                    j = pos[sorted_vals[i]]
                    vals[i], vals[j] = vals[j], vals[i]
                    pos[vals[j]] = j
                    pos[vals[i]] = i
                    ans += 1
        return ans
