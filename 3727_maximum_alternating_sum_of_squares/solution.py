# LeetCode 3727 - Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = [x * x for x in nums]
        a.sort()
        m = len(a) // 2
        ans = 0
        for i in range(m):
            ans -= a[i]
        for i in range(m, len(a)):
            ans += a[i]
        return ans
