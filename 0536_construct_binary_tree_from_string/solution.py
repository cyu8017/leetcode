# LeetCode 0536 - Construct Binary Tree from String
# https://leetcode.com/problems/construct-binary-tree-from-string/

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
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        index = 0

        def parse() -> Optional[TreeNode]:
            nonlocal index
            if index >= len(s):
                return None

            sign = 1
            if s[index] == "-":
                sign = -1
                index += 1

            value = 0
            while index < len(s) and s[index].isdigit():
                value = value * 10 + int(s[index])
                index += 1

            node = TreeNode(sign * value)

            if index < len(s) and s[index] == "(":
                index += 1
                node.left = parse()
                index += 1

            if index < len(s) and s[index] == "(":
                index += 1
                node.right = parse()
                index += 1

            return node

        return parse()
