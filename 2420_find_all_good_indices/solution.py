# LeetCode 2420 - Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/

from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dec = [0] * n
        inc = [0] * n
        dec[0] = 1
        for i in range(1, n):
            dec[i] = dec[i - 1] + 1 if nums[i] <= nums[i - 1] else 1
        inc[n - 1] = 1
        for i in range(n - 2, -1, -1):
            inc[i] = inc[i + 1] + 1 if nums[i] <= nums[i + 1] else 1
        ans = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                ans.append(i)
        return ans
