# LeetCode 2427 - Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        ans = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                ans += 1
                if i * i != g:
                    ans += 1
            i += 1
        return ans
