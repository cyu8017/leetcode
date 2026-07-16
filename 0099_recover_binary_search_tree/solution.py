# LeetCode 0099 - Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        previous = None
        stack: list[TreeNode] = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if previous and previous.val > current.val:
                if first is None:
                    first = previous
                second = current
            previous = current
            current = current.right

        if first and second:
            first.val, second.val = second.val, first.val
