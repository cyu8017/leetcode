// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

public class Solution {
    const int MOD = 1000000007;

    public int CountGoodNumbers(long n) {
        return (int)(ModPow(5, (n + 1) / 2) * ModPow(4, n / 2) % MOD);
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