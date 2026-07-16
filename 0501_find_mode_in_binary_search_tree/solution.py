# LeetCode 0501 - Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        counts: dict[int, int] = {}
        best = 0

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal best
            if not node:
                return
            inorder(node.left)
            counts[node.val] = counts.get(node.val, 0) + 1
            best = max(best, counts[node.val])
            inorder(node.right)

        inorder(root)
        return [value for value, count in counts.items() if count == best]
