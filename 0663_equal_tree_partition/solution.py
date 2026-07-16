# LeetCode 0663 - Equal Tree Partition
# https://leetcode.com/problems/equal-tree-partition/

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
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        subtree_sums: list[int] = []

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(total)
            return total

        total = dfs(root)
        subtree_sums.pop()
        return total % 2 == 0 and (total // 2) in subtree_sums
