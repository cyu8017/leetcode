# LeetCode 0654 - Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/

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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = left
            for i in range(left, right + 1):
                if nums[i] > nums[mid]:
                    mid = i
            return TreeNode(
                nums[mid],
                build(left, mid - 1),
                build(mid + 1, right),
            )

        return build(0, len(nums) - 1)
