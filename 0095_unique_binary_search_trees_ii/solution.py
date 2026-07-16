# LeetCode 0095 - Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            trees: List[Optional[TreeNode]] = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n) if n else []
