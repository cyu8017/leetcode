// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
public:
    int maxNiceDivisors(int primeFactors) {
        if (primeFactors <= 3) {
            return primeFactors;
        }
        const int MOD = 1000000007;
        if (primeFactors % 3 == 0) {
            return static_cast<int>(powMod(3, primeFactors / 3, MOD));
        }
        if (primeFactors % 3 == 1) {
            return static_cast<int>(powMod(3, primeFactors / 3 - 1, MOD) * 4 % MOD);
        }
        return static_cast<int>(powMod(3, primeFactors / 3, MOD) * 2 % MOD);
    }

private:
    long long powMod(long long base, long long exp, long long mod) {
        long long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }
};
