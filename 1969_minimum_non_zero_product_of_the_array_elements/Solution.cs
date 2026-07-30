// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

public class Solution {
    const int MOD = 1000000007;

    public int MinNonZeroProduct(int p) {
        long mx = (1L << p) - 1;
        return (int)(mx % MOD * ModPow(mx - 1, (1L << (p - 1)) - 1) % MOD);
    }

    long ModPow(long x, long e) {
        long r = 1;
        x %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) r = r * x % MOD;
            x = x * x % MOD;
            e >>= 1;
        }
        return r;
    }
}