# LeetCode 3961 - Maximize Sum Of Device Ratings
# https://leetcode.com/problems/maximize-sum-of-device-ratings/

from typing import List


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        n = len(units[0])
        if n == 1:
            ans = 0
            for x in units:
                ans += x[0]
            return ans
        answer = 0
        mn = 2147483647
        mn2 = 2147483647
        for x in units:
            x.sort()
            answer += x[1]
            mn2 = min(mn2, x[1])
            mn = min(mn, x[0])
        return answer - (mn2 - mn)
