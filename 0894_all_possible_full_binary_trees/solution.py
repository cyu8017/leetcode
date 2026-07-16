# LeetCode 0894 - All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


from functools import lru_cache


class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        @lru_cache(None)
        def build(nodes: int) -> tuple:
            if nodes % 2 == 0:
                return ()
            if nodes == 1:
                return (TreeNode(0),)
            res = []
            for left in range(1, nodes, 2):
                right = nodes - 1 - left
                for L in build(left):
                    for R in build(right):
                        root = TreeNode(0)
                        root.left = L
                        root.right = R
                        res.append(root)
            return tuple(res)

        return list(build(n))
