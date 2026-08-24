# LeetCode 3997 - Count Dominant Nodes in a Binary Tree
# https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -2147483648
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        mx = max(max(l, r), node.val)
        if mx == node.val:
            self.ans += 1
        return mx

    def countDominantNodes(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
