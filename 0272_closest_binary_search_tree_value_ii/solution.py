# LeetCode 0272 - Closest Binary Search Tree Value II
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/

import bisect
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(
        self, root: Optional[TreeNode], target: float, k: int
    ) -> List[int]:
        values: list[int] = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        index = bisect.bisect_left(values, target)
        left = index - 1
        right = index
        result: list[int] = []
        while len(result) < k:
            if right >= len(values) or (
                left >= 0
                and abs(values[left] - target) <= abs(values[right] - target)
            ):
                result.append(values[left])
                left -= 1
            else:
                result.append(values[right])
                right += 1
        return result
