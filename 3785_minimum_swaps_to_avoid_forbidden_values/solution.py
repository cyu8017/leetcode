# LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

from typing import List


class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        for x in forbidden:
            freq[x] = freq.get(x, 0) + 1
        for c in freq.values():
            if c > n:
                return -1
        bad = {}
        total = 0
        largest = 0
        for i in range(n):
            if nums[i] == forbidden[i]:
                bad[nums[i]] = bad.get(nums[i], 0) + 1
                total += 1
                if bad[nums[i]] > largest:
                    largest = bad[nums[i]]
        if (total + 1) // 2 > largest:
            return (total + 1) // 2
        return largest
