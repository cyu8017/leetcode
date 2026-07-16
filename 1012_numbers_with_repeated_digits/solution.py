# LeetCode 1012 - Numbers With Repeated Digits
# https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n)))
        m = len(digits)

        def p(a: int, b: int) -> int:
            res = 1
            for i in range(b):
                res *= a - i
            return res

        # numbers with fewer digits than n
        total_unique = 0
        for length in range(1, m):
            total_unique += 9 * p(9, length - 1)

        used = set()
        for i, d in enumerate(digits):
            for x in range(0 if i else 1, d):
                if x in used:
                    continue
                total_unique += p(9 - i, m - i - 1)
            if d in used:
                break
            used.add(d)
        else:
            total_unique += 1
        return n - total_unique
