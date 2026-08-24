# LeetCode 3936 - Minimum Swaps To Move Zeros To End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            while i < n and nums[i] != 0:
                i += 1
            while j > 0 and nums[j] == 0:
                j -= 1
            if i >= j:
                break
            ans += 1
            i += 1
            j -= 1
        return ans
