// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

static long long powMod(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}

int maxNiceDivisors(int primeFactors) {
    const long long MOD = 1000000007LL;
    if (primeFactors <= 3) return primeFactors;
    if (primeFactors % 3 == 0) {
        return (int)powMod(3, primeFactors / 3, MOD);
    }
    if (primeFactors % 3 == 1) {
        return (int)(powMod(3, primeFactors / 3 - 1, MOD) * 4 % MOD);
    }
    return (int)(powMod(3, primeFactors / 3, MOD) * 2 % MOD);
}
