# LeetCode 0671 - Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        ans = -1

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal ans
            if not node:
                return
            if node.val > root.val:
                if ans == -1 or node.val < ans:
                    ans = node.val
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
