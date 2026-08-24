# LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = special[0] - bottom
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)
        ans = max(ans, top - special[-1])
        return ans
