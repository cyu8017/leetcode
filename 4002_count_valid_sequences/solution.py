# LeetCode 4002 - Count Valid Sequences
# https://leetcode.com/problems/count-valid-sequences/


class Solution:
    MX = 500001
    MOD = 1000000007
    f = None
    g = None
    inited = False

    def modPow(self, a: int, b: int) -> int:
        res = 1
        a %= self.MOD
        while b > 0:
            if (b & 1) != 0:
                res = res * a % self.MOD
            a = a * a % self.MOD
            b >>= 1
        return res

    def ensureInit(self) -> None:
        if Solution.inited:
            return
        Solution.inited = True
        Solution.f = [0] * Solution.MX
        Solution.g = [0] * Solution.MX
        Solution.f[0] = 1
        Solution.g[0] = 1
        for i in range(1, Solution.MX):
            Solution.f[i] = Solution.f[i - 1] * i % Solution.MOD
            Solution.g[i] = self.modPow(Solution.f[i], Solution.MOD - 2)

    def comb(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        return Solution.f[n] * Solution.g[k] % Solution.MOD * Solution.g[n - k] % Solution.MOD

    def countValidSequences(self, n: int, k: int) -> int:
        self.ensureInit()
        ans = self.comb(n - 1, k - 1)
        if (n + k) % 2 == 0:
            ans = (ans - self.comb((n + k) // 2 - 1, k - 1) + self.MOD) % self.MOD
        return ans
