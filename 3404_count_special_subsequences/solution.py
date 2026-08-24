# LeetCode 3404 - Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/

from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 2, n):
                for k in range(j + 2, n):
                    for l in range(k + 2, n):
                        if nums[i] * nums[k] == nums[j] * nums[l]:
                            ans += 1
        return ans
