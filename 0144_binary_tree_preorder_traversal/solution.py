# LeetCode 0144 - Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
