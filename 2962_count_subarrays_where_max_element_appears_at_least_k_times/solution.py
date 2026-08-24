# LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = nums[0]
        for v in nums:
            if v > mx:
                mx = v
        ans = 0
        cnt = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == mx:
                cnt += 1
            while cnt >= k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
