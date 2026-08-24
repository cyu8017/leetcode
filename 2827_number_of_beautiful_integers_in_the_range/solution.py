# LeetCode 2827 - Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            s = str(n)
            memo = [
                [[[[-1] * 2 for _ in range(2)] for _ in range(22)] for _ in range(45)]
                for _ in range(12)
            ]

            def dfs(pos: int, diff: int, mod: int, tight: int, started: int) -> int:
                if pos == len(s):
                    return 1 if started and diff == 0 and mod == 0 else 0
                if memo[pos][diff + 20][mod][tight][started] != -1:
                    return memo[pos][diff + 20][mod][tight][started]
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for digit in range(up + 1):
                    nt = 1 if tight and digit == up else 0
                    if not started:
                        if digit == 0:
                            ans += dfs(pos + 1, diff, mod, nt, 0)
                        else:
                            nd = diff + (1 if digit % 2 == 0 else -1)
                            ans += dfs(pos + 1, nd, digit % k, nt, 1)
                    else:
                        nd = diff + (1 if digit % 2 == 0 else -1)
                        ans += dfs(pos + 1, nd, (mod * 10 + digit) % k, nt, 1)
                memo[pos][diff + 20][mod][tight][started] = ans
                return ans

            return dfs(0, 0, 0, 1, 0)

        return count(high) - count(low - 1)
