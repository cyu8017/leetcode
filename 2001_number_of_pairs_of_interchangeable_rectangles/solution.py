# LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        freq = {}
        ans = 0
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            f = freq.get(key, 0)
            ans += f
            freq[key] = f + 1
        return ans
