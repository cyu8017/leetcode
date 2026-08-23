// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

public class Solution {
    static long Qpow(long a, long n, long mod) {
        a %= mod;
        long ans = 1;
        while (n > 0) {
            if ((n & 1) != 0) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }

    public int SumOfNumbers(int l, int r, int k) {
        const long MOD = 1000000007;
        long n = r - l + 1;
        long sum = (long)(l + r) * n / 2 % MOD;
        long part1 = Qpow(n % MOD, k - 1, MOD);
        long part2 = (Qpow(10, k, MOD) - 1 + MOD) % MOD;
        long inv9 = Qpow(9, MOD - 2, MOD);
        long ans = sum;
        ans = ans * part1 % MOD;
        ans = ans * part2 % MOD;
        ans = ans * inv9 % MOD;
        return (int)ans;
    }
}
