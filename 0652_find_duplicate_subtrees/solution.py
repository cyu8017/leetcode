# LeetCode 0652 - Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/

from collections import defaultdict
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
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        counts: dict[str, int] = defaultdict(int)
        result: list[Optional[TreeNode]] = []

        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            counts[key] += 1
            if counts[key] == 2:
                result.append(node)
            return key

        serialize(root)
        return result
