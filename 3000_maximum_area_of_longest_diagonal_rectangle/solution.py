# LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        mx = 0
        for d in dimensions:
            l, w = d[0], d[1]
            t = l * l + w * w
            if mx < t:
                mx = t
                ans = l * w
            elif mx == t:
                ans = max(ans, l * w)
        return ans
