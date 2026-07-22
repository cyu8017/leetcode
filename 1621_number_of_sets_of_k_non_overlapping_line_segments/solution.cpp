// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution {
    static long long modPow(long long base, long long exp, long long mod) {
        long long r = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) {
                r = r * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return r;
    }

    static long long comb(int n, int k, long long mod) {
        if (k < 0 || k > n) {
            return 0;
        }
        long long num = 1, den = 1;
        for (int i = 0; i < k; ++i) {
            num = num * (n - i) % mod;
            den = den * (i + 1) % mod;
        }
        return num * modPow(den, mod - 2, mod) % mod;
    }

public:
    int numberOfSets(int n, int k) {
        const long long MOD = 1000000007;
        return static_cast<int>(comb(n + k - 1, 2 * k, MOD));
    }
};
