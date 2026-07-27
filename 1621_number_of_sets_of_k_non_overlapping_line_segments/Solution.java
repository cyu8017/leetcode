// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfSets(int n, int k) {
        return (int) comb(n + k - 1, 2 * k);
    }

    private long comb(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = Math.min(r, n - r);
        long num = 1, den = 1;
        for (int i = 1; i <= r; i++) {
            num = num * (n - r + i) % MOD;
            den = den * i % MOD;
        }
        return num * modPow(den, MOD - 2) % MOD;
    }

    private long modPow(long base, long exp) {
        long res = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
}
