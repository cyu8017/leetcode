# LeetCode 2750 - Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 1000000007
        ones = [i for i, v in enumerate(nums) if v == 1]
        if not ones:
            return 0
        ans = 1
        for i in range(1, len(ones)):
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        return ans
