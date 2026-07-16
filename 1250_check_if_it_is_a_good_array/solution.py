from math import gcd
from functools import reduce

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        return reduce(gcd, nums) == 1
