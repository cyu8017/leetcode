from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 1_000_000_007
        diff = [0] * (len(nums) + 1)
        for left, right in requests:
            diff[left] += 1
            diff[right + 1] -= 1
        for i in range(1, len(nums)):
            diff[i] += diff[i - 1]
        return sum(a * b for a, b in zip(sorted(nums), sorted(diff[:-1]))) % MOD
