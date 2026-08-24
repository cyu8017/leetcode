# LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            r = 0
            while x > 0:
                r = r * 10 + x % 10
                x //= 10
            return r

        seen = set()
        for x in nums:
            seen.add(x)
            seen.add(rev(x))
        return len(seen)
