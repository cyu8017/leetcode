// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution {
    static final int MOD = 1_000_000_007;

    public int minNonZeroProduct(int p) {
        long mx = (1L << p) - 1;
        return (int) (mx % MOD * modPow((mx - 1) % MOD, (1L << (p - 1)) - 1) % MOD);
    }

    private long modPow(long a, long e) {
        long r = 1;
        while (e > 0) {
            if ((e & 1) == 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
}
