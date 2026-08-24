# LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
# https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if node.left is None and node.right is None:
                return [0, 1] if node.val == 0 else [1, 0]
            if node.val == 5:
                x = dfs(node.left)
                return [x[1], x[0]]
            L, R = dfs(node.left), dfs(node.right)
            lf, lt, rf, rt = L[0], L[1], R[0], R[1]
            if node.val == 2:
                return [lf + rf, min(lt + rt, lt + rf, lf + rt)]
            if node.val == 3:
                return [min(lf + rf, lf + rt, lt + rf), lt + rt]
            if node.val == 4:
                return [min(lf + rf, lt + rt), min(lf + rt, lt + rf)]
            return [0, 0]

        res = dfs(root)
        return res[1] if result else res[0]
