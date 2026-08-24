# LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        def lower_bound(q: int) -> int:
            lo, hi = 0, len(vals)
            while lo < hi:
                mid = (lo + hi) >> 1
                if vals[mid] < q:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = []
        for q in queries:
            j = lower_bound(q)
            mx = vals[j] if j < len(vals) else -1
            mn = -1
            if j < len(vals) and vals[j] == q:
                mn = q
            elif j > 0:
                mn = vals[j - 1]
            ans.append([mn, mx])
        return ans
