class Solution:
    def numOfWays(self, n):
        mod = 1_000_000_007
        aba = abc = 6
        for _ in range(1, n):
            aba, abc = (3 * aba + 2 * abc) % mod, (2 * aba + 2 * abc) % mod
        return (aba + abc) % mod
