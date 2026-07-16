# LeetCode 0179 - Largest Number
# https://leetcode.com/problems/largest-number/

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        parts = [str(num) for num in nums]

        def compare(a: str, b: str) -> int:
            left, right = a + b, b + a
            if left > right:
                return -1
            if left < right:
                return 1
            return 0

        parts.sort(key=cmp_to_key(compare))
        if parts[0] == "0":
            return "0"
        return "".join(parts)
