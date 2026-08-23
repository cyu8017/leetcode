// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

#include <cstdint>

class Solution {
    static int64_t qpow(int64_t a, int64_t n, int64_t mod) {
        a %= mod;
        int64_t ans = 1;
        while (n > 0) {
            if (n & 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }

public:
    int sumOfNumbers(int l, int r, int k) {
        const int64_t MOD = 1000000007;
        int64_t n = r - l + 1;
        int64_t sum = (int64_t)(l + r) * n / 2 % MOD;
        int64_t part1 = qpow(n % MOD, k - 1, MOD);
        int64_t part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD;
        int64_t inv9 = qpow(9, MOD - 2, MOD);
        int64_t ans = sum;
        ans = ans * part1 % MOD;
        ans = ans * part2 % MOD;
        ans = ans * inv9 % MOD;
        return (int)ans;
    }
};
