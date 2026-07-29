// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

static long long modPow(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = res * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return res;
}

int countGoodNumbers(long long n) {
    const long long MOD = 1000000007LL;
    return (int)(modPow(5, (n + 1) / 2, MOD) * modPow(4, n / 2, MOD) % MOD);
}
