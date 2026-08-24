# LeetCode 2117 - Abbreviating the Product of a Range
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/

import math
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        twos = 0
        fives = 0
        for i in range(left, (right) + 1):
            x = i
            while x % 2 == 0:
                twos += 1
                x = x // 2
            while x % 5 == 0:
                fives += 1
                x = x // 5
        zeros = min(twos, fives)
        MOD = 100000000000
        prod = 1
        extra2 = twos - zeros
        extra5 = fives - zeros
        logSum = 0
        for i in range(left, (right) + 1):
            x = i
            while x % 2 == 0:
                x = x // 2
            while x % 5 == 0:
                x = x // 5
            prod = (prod * x) % MOD
            logSum += math.log10(x)
        for i in range(extra2):
            prod = (prod * 2) % MOD
            logSum += math.log10(2)
        for i in range(extra5):
            prod = (prod * 5) % MOD
            logSum += math.log10(5)
        fullLog = 0
        for i in range(left, (right) + 1):
            fullLog += math.log10(i)
        digits = math.floor(fullLog) + 1
        if digits <= 10:
            p = 1
            for i in range(left, (right) + 1):
                p *= i
            return str(p)
        frac = logSum - math.floor(logSum)
        prefix = math.floor((10) ** (frac + 4))
        suffix = prod % 100000
        return str(prefix) + "e" + str(zeros) + str(suffix).zfill(5)
