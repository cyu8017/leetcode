# LeetCode 2999 - Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num: int) -> int:
            if num < 0:
                return 0
            for i in range(len(s)):
                if ord(s[i]) - 48 > limit:
                    return 0
            t = str(num)
            n = len(t)
            sn = len(s)
            if n < sn:
                return 0
            ans = 0
            for length in range(sn, n):
                preLen = length - sn
                if preLen == 0:
                    ans += 1
                else:
                    ways = limit
                    for i in range(1, preLen):
                        ways *= limit + 1
                    ans += ways
            pref = n - sn
            memo = {}

            def dfs(i: int, tight: bool) -> int:
                if i == pref:
                    if tight:
                        return 1 if t[pref:] >= s else 0
                    return 1
                key = (i << 1) | (1 if tight else 0)
                if key in memo:
                    return memo[key]
                up = (ord(t[i]) - 48) if tight else limit
                if up > limit:
                    up = limit
                res = 0
                for d in range(up + 1):
                    if i == 0 and d == 0:
                        continue
                    res += dfs(i + 1, tight and d == (ord(t[i]) - 48))
                memo[key] = res
                return res

            ans += dfs(0, True)
            return ans

        return count(finish) - count(start - 1)
