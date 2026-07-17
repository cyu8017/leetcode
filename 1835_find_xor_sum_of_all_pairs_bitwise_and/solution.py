# LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

from functools import reduce
from operator import xor


class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        xor1 = reduce(xor, arr1, 0)
        xor2 = reduce(xor, arr2, 0)
        return xor1 & xor2
