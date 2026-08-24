# LeetCode 3837 - Delayed Count of Equal Elements
# https://leetcode.com/problems/delayed-count-of-equal-elements/

from typing import List


class Solution:
    def delayedCount(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = {}
        ans = [0] * n
        for i in range(n - k - 2, -1, -1):
            key = nums[i + k + 1]
            cnt[key] = cnt.get(key, 0) + 1
            ans[i] = cnt.get(nums[i], 0)
        return ans
