// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

class Solution {
    static final int MOD = 1_000_000_007;

    public int countGoodNumbers(long n) {
        return (int) (modPow(5, (n + 1) / 2) * modPow(4, n / 2) % MOD);
    }

    private long modPow(long a, long e) {
        long r = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
}
