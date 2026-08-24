# LeetCode 3255 - Find the Power of K-Size Subarrays II
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        if k == 1:
            return nums[:]
        streak = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1
            if i >= k - 1:
                ans[i - k + 1] = nums[i] if streak >= k else -1
        return ans
