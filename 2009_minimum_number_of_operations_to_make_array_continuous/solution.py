# LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        uniq = sorted(set(nums))
        ans, j = n, 0
        for i in range(len(uniq)):
            while j < len(uniq) and uniq[j] - uniq[i] + 1 <= n:
                j += 1
            ans = min(ans, n - (j - i))
        return ans
