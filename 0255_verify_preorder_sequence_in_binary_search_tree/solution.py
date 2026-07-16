# LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        low = float("-inf")
        stack: list[int] = []
        for value in preorder:
            if value < low:
                return False
            while stack and stack[-1] < value:
                low = stack.pop()
            stack.append(value)
        return True
