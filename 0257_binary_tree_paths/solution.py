# LeetCode 0257 - Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result: list[str] = []

        def dfs(node: Optional[TreeNode], path: list[str]) -> None:
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return result
