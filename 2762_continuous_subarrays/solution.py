# LeetCode 2762 - Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        min_q = []
        max_q = []
        for right, val in enumerate(nums):
            while min_q and nums[min_q[-1]] > val:
                min_q.pop()
            while max_q and nums[max_q[-1]] < val:
                max_q.pop()
            min_q.append(right)
            max_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if min_q[0] < left:
                    min_q.pop(0)
                if max_q[0] < left:
                    max_q.pop(0)
            ans += right - left + 1
        return ans
