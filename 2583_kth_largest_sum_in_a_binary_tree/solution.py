# LeetCode 2583 - Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        sums = []
        q = deque([root])
        while q:
            sz = len(q)
            s = 0
            for _ in range(sz):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(s)
        sums.sort(reverse=True)
        if k > len(sums):
            return -1
        return sums[k - 1]
