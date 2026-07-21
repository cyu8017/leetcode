class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        mx = (1 << p) - 1
        return (mx * pow(mx - 1, (1 << (p - 1)) - 1, MOD)) % MOD
