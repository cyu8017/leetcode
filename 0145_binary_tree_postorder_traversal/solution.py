# LeetCode 0145 - Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result
