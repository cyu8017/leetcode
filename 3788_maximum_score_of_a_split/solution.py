# LeetCode 3788 - Maximum Score of a Split
# https://leetcode.com/problems/maximum-score-of-a-split/

from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])
        pre = 0
        ans = -(10**18)
        for i in range(n - 1):
            pre += nums[i]
            ans = max(ans, pre - suf[i + 1])
        return ans
