# LeetCode 3352 - Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/


def bitsPop(x: int) -> int:
    c = 0
    while x > 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 1000000007
        red = [0] * 801
        red[1] = 0
        for i in range(2, 801):
            red[i] = 1 + red[bitsPop(i)]
        memo = {}

        def key(pos: int, tight: int, ones: int) -> int:
            return (pos << 32) | (tight << 16) | ones

        def dfs(pos: int, tight: bool, ones: int) -> int:
            if pos == len(s):
                if ones == 0:
                    return 0
                return 1 if red[ones] <= k - 1 else 0
            ky = key(pos, 1 if tight else 0, ones)
            if ky in memo:
                return memo[ky]
            up = (ord(s[pos]) - 48) if tight else 1
            ans = 0
            for d in range(up + 1):
                nt = tight and d == up
                ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
            memo[ky] = ans
            return ans

        return dfs(0, True, 0)
