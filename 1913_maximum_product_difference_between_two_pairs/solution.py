from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = b = 0
        c = d = 10**5
        for x in nums:
            if x > a:
                b, a = a, x
            elif x > b:
                b = x
            if x < c:
                d, c = c, x
            elif x < d:
                d = x
        return a * b - c * d
