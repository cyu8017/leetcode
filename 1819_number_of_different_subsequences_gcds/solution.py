# LeetCode 1819 - Number of Different Subsequences GCDs
# https://leetcode.com/problems/number-of-different-subsequences-gcds/

import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        present = [False] * (max_val + 1)
        for num in nums:
            present[num] = True

        ans = 0
        for g in range(1, max_val + 1):
            has = False
            gcd_val = 0
            for multiple in range(g, max_val + 1, g):
                if present[multiple]:
                    has = True
                    gcd_val = math.gcd(gcd_val, multiple // g)
                    if gcd_val == 1:
                        break
            if has and gcd_val == 1:
                ans += 1
        return ans
