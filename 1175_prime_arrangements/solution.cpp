// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
public:
    int numPrimeArrangements(int n) {
        const int MOD = 1e9 + 7;
        auto isPrime = [](int x) {
            if (x < 2) return false;
            for (int d = 2; d * d <= x; ++d) if (x % d == 0) return false;
            return true;
        };
        int primes = 0;
        for (int i = 1; i <= n; ++i) if (isPrime(i)) ++primes;
        auto fact = [&](int x) {
            long long res = 1;
            for (int i = 2; i <= x; ++i) res = res * i % MOD;
            return res;
        };
        return static_cast<int>(fact(primes) * fact(n - primes) % MOD);
    }
};
