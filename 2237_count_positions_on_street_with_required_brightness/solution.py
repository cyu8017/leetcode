# LeetCode 2237 - Count Positions on Street With Required Brightness
# https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

from typing import List


class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        diff = [0] * (n + 1)
        for pos, r in lights:
            l = max(0, pos - r)
            rr = min(n - 1, pos + r)
            diff[l] += 1
            diff[rr + 1] -= 1
        ans = cur = 0
        for i in range(n):
            cur += diff[i]
            if cur >= requirement[i]:
                ans += 1
        return ans
