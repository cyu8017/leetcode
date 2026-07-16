# LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            if ld > rd:
                return ld + 1, ln
            if rd > ld:
                return rd + 1, rn
            return ld + 1, node

        return dfs(root)[1]
