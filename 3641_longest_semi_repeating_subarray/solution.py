# LeetCode 3641 - Longest Semi-Repeating Subarray
# https://leetcode.com/problems/longest-semi-repeating-subarray/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        cnt = {}
        ans = 0
        cur = 0
        l = 0
        for r, x in enumerate(nums):
            c = cnt.get(x, 0) + 1
            cnt[x] = c
            if c == 2:
                cur += 1
            while cur > k:
                c2 = cnt.get(nums[l], 0) - 1
                cnt[nums[l]] = c2
                if c2 == 1:
                    cur -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
