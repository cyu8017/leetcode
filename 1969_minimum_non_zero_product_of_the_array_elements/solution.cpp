// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
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
    int minNonZeroProduct(int p) {
        long long mx = (1LL << p) - 1;
        return (int)(mx % MOD * modPow(mx - 1, (1LL << (p - 1)) - 1) % MOD);
    }
};
