# LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        ans = n
        for p in pos.values():
            max_gap = 0
            for i in range(len(p)):
                gap = p[i + 1] - p[i] if i + 1 < len(p) else p[0] + n - p[i]
                max_gap = max(max_gap, gap // 2)
            ans = min(ans, max_gap)
        return ans
