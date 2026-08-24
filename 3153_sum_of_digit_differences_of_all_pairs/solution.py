# LeetCode 3153 - Sum of Digit Differences of All Pairs
# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        x = nums[0]
        while x > 0:
            m += 1
            x //= 10
        if m == 0:
            m = 1
        ans = 0
        vals = nums[:]
        for _ in range(m):
            cnt = [0] * 10
            for i in range(n):
                cnt[vals[i] % 10] += 1
                vals[i] //= 10
            for v in cnt:
                ans += v * (n - v)
        return ans // 2
