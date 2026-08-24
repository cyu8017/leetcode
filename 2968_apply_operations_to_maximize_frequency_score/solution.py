# LeetCode 2968 - Apply Operations to Maximize Frequency Score
# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

from typing import List


def costRange(nums: List[int], pref: List[int], l: int, r: int) -> int:
    mid = (l + r) >> 1
    left = nums[mid] * (mid - l) - (pref[mid] - pref[l])
    right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid)
    return left + right


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 1
        left = 0
        for right in range(n):
            while costRange(nums, pref, left, right) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans
