# LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
# https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def f(k: int, mn: int, mx: int) -> List[int]:
            cnt = 0
            a = float("inf")
            b = float("-inf")
            for i in range(len(nums)):
                x = nums[i]
                if ((x - i) & 1) != k:
                    cnt += 1
                    if x == mn:
                        x += 1
                    elif x == mx:
                        x -= 1
                a = min(a, x)
                b = max(b, x)
            return [cnt, max(1, int(b - a))]

        if len(nums) == 1:
            return [0, 0]
        mn = nums[0]
        mx = nums[0]
        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)
        r0 = f(0, mn, mx)
        r1 = f(1, mn, mx)
        if r0[0] != r1[0]:
            return r0 if r0[0] < r1[0] else r1
        return r0 if r0[1] <= r1[1] else r1
