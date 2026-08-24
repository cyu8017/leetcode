# LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x //= 10
            return y

        n = len(nums)
        pos = {}
        ans = n + 1
        for i, val in enumerate(nums):
            if val in pos:
                ans = min(ans, i - pos[val])
            pos[reverse(val)] = i
        return -1 if ans > n else ans
