# LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node):
            if not node:
                return [0, 0, 1]
            L = dfs(node.left)
            R = dfs(node.right)
            sz = L[1] + R[1] + 1
            perf = L[2] == 1 and R[2] == 1 and L[0] == R[0]
            if perf:
                sizes.append(sz)
            return [max(L[0], R[0]) + 1, sz, 1 if perf else 0]

        dfs(root)
        sizes.sort(reverse=True)
        if k > len(sizes):
            return -1
        return sizes[k - 1]
