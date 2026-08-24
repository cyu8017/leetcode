# LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for bit in range(24):
            cnt = 0
            for x in candidates:
                if (x >> bit) & 1:
                    cnt += 1
            ans = max(ans, cnt)
        return ans
