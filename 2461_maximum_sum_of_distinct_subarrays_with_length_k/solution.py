# LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = {}
        total = 0
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
            if i >= k:
                y = nums[i - k]
                total -= y
                c = cnt[y] - 1
                if c == 0:
                    del cnt[y]
                else:
                    cnt[y] = c
            if i >= k - 1 and len(cnt) == k and total > ans:
                ans = total
        return ans
