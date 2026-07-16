# LeetCode 0164 - Maximum Gap
# https://leetcode.com/problems/maximum-gap/

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        low, high = min(nums), max(nums)
        if low == high:
            return 0
        n = len(nums)
        bucket_size = max(1, (high - low) // (n - 1))
        bucket_count = (high - low) // bucket_size + 1
        mins = [float("inf")] * bucket_count
        maxs = [float("-inf")] * bucket_count
        used = [False] * bucket_count
        for num in nums:
            idx = (num - low) // bucket_size
            used[idx] = True
            mins[idx] = min(mins[idx], num)
            maxs[idx] = max(maxs[idx], num)
        best = 0
        prev_max = low
        for i in range(bucket_count):
            if not used[i]:
                continue
            best = max(best, mins[i] - prev_max)
            prev_max = maxs[i]
        return int(best)
