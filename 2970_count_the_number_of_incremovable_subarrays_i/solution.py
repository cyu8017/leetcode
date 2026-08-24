# LeetCode 2970 - Count the Number of Incremovable Subarrays I
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                prev = -1
                ok = True
                for t in range(n):
                    if t >= i and t <= j:
                        continue
                    if nums[t] <= prev:
                        ok = False
                        break
                    prev = nums[t]
                if ok:
                    ans += 1
        return ans
