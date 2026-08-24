# LeetCode 2389 - Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid] <= q:
                    lo = mid + 1
                else:
                    hi = mid
            ans[i] = lo
        return ans
