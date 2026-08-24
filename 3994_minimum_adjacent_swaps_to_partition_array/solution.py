# LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

from typing import List


class Solution:
    def minAdjacentSwaps(self, nums: List[int], a: int, b: int) -> int:
        MOD = 1000000007
        result = 0
        cnt1 = 0
        cnt2 = 0
        for x in nums:
            if x < a:
                result = (result + cnt1 + cnt2) % MOD
            elif x <= b:
                cnt1 += 1
                result = (result + cnt2) % MOD
            else:
                cnt2 += 1
        return result
