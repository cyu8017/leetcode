# LeetCode 2367 - Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        ans = 0
        for x in nums:
            if (x + diff) in seen and (x + 2 * diff) in seen:
                ans += 1
        return ans
