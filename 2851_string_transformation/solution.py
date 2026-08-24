# LeetCode 2851 - String Transformation
# https://leetcode.com/problems/string-transformation/


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 1000000007
        n = len(s)
        ss = s + s
        if t not in ss[: 2 * n - 1]:
            return 0
        cnt = 0
        for i in range(n):
            if ss[i : i + n] == t:
                cnt += 1
        same = s == t

        def mod_pow(a: int, b: int) -> int:
            res = 1
            a %= MOD
            bb = b
            while bb > 0:
                if bb & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                bb >>= 1
            return res

        pk = mod_pow(n - 1, k)
        invn = mod_pow(n, MOD - 2)
        sign = MOD - 1 if k % 2 == 1 else 1
        ways_same = ((pk + (n - 1) * sign % MOD) % MOD * invn) % MOD
        ways_diff = ((pk - sign + MOD) % MOD * invn) % MOD
        if same:
            return (ways_same + ways_diff * (cnt - 1)) % MOD
        return (ways_diff * cnt) % MOD
