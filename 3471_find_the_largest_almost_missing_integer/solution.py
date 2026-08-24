# LeetCode 3471 - Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = {}
        for i in range(n - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for x in seen:
                cnt[x] = cnt.get(x, 0) + 1
        ans = -1
        for key, value in cnt.items():
            if value == 1 and key > ans:
                ans = key
        return ans
