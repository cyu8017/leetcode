// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

class Solution {
    static constexpr long long MOD = 1000000007;
    long long modPow(long long a, long long e) {
        long long r = 1;
        a %= MOD;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
public:
    int countGoodNumbers(long long n) {
        return (int)(modPow(5, (n + 1) / 2) * modPow(4, n / 2) % MOD);
    }
};
