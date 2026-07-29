// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

static long long modPow(long long base, long long exp, long long mod) {
    long long res = 1 % mod;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

int minNonZeroProduct(int p) {
    const long long MOD = 1000000007LL;
    long long mx = (1LL << p) - 1;
    long long pairs = mx / 2;
    return (int)(modPow(mx - 1, pairs, MOD) * (mx % MOD) % MOD);
}
