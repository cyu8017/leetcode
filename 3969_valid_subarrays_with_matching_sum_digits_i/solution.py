# LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

from typing import List


class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            s = 0
            for r in range(l, n):
                s += nums[r]
                if s % 10 == x:
                    t = str(s)
                    if ord(t[0]) - 48 == x:
                        ans += 1
        return ans
