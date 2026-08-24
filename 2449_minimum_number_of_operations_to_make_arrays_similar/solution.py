# LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        odd_n, even_n, odd_t, even_t = [], [], [], []
        for x in nums:
            (even_n if x % 2 == 0 else odd_n).append(x)
        for x in target:
            (even_t if x % 2 == 0 else odd_t).append(x)
        ans = 0
        for i in range(len(odd_n)):
            diff = odd_n[i] - odd_t[i]
            if diff > 0:
                ans += diff // 2
        for i in range(len(even_n)):
            diff = even_n[i] - even_t[i]
            if diff > 0:
                ans += diff // 2
        return ans
