# LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        cnt = 0
        for x in nums:
            if x % 6 == 0:
                total += x
                cnt += 1
        return 0 if cnt == 0 else total // cnt
