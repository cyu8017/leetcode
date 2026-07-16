# LeetCode 0776 - Split BST
# https://leetcode.com/problems/split-bst/

from typing import List, Optional


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
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val <= target:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        left, right = self.splitBST(root.left, target)
        root.left = right
        return [left, root]
