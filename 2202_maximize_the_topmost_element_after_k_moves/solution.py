# LeetCode 2202 - Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

from typing import List
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return -1 if k % 2 != 0 else nums[0]
        if k == 0:
            return nums[0]
        ans = -1
        limit = min(k - 1, n)
        for i in range(limit):
            ans = max(ans, nums[i])
        if k < n:
            ans = max(ans, nums[k])
        return ans
