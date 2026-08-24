# LeetCode 2670 - Find the Distinct Difference Array
# https://leetcode.com/problems/find-the-distinct-difference-array/

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [0] * (n + 1)
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(nums[i])
            suf[i] = len(seen)
        seen.clear()
        ans = [0] * n
        for i in range(n):
            seen.add(nums[i])
            ans[i] = len(seen) - suf[i + 1]
        return ans
