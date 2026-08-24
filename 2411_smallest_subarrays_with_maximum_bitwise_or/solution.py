# LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last = [-1] * 32
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if ((nums[i] >> b) & 1) != 0:
                    last[b] = i
            far = i
            for b in range(32):
                far = max(far, last[b])
            ans[i] = far - i + 1
        return ans
