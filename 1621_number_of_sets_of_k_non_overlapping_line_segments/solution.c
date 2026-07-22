// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

#define MOD 1000000007LL

static long long modPow(long long base, long long exp) {
    long long r = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) r = r * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    return r;
}

static long long comb(long long n, long long k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    long long num = 1, den = 1;
    for (long long i = 1; i <= k; i++) {
        num = num * ((n - k + i) % MOD) % MOD;
        den = den * (i % MOD) % MOD;
    }
    return num * modPow(den, MOD - 2) % MOD;
}

int numberOfSets(int n, int k) {
    return (int)comb(n + k - 1, 2LL * k);
}
