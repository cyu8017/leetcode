# LeetCode 2961 - Double Modular Exponentiation
# https://leetcode.com/problems/double-modular-exponentiation/

from typing import List


def modPow(a: int, b: int, mod: int) -> int:
    res = 1 % mod
    a %= mod
    while b > 0:
        if (b & 1) != 0:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i in range(len(variables)):
            v = variables[i]
            a, b, c, m = v[0], v[1], v[2], v[3]
            if modPow(modPow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans
