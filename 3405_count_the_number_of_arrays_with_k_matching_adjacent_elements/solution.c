// LeetCode 3405 - Count the Number of Arrays With K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

static int modPow3405(long long a, long long e, int mod) {
    long long r = 1; a %= mod; if (a < 0) a = 0;
    while (e > 0) { if (e & 1) r = r * a % mod; a = a * a % mod; e >>= 1; }
    return (int)r;
}
static int comb3405(int n, int k, int mod) {
    if (k < 0 || k > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < k; i++) { num = num * (n - i) % mod; den = den * (i + 1) % mod; }
    return (int)(num * modPow3405(den, mod - 2, mod) % mod);
}
int countGoodArrays(int n, int m, int k) {
    const int mod = 1000000007;
    return (int)((long long)comb3405(n - 1, k, mod) * m % mod * modPow3405(m - 1, n - 1 - k, mod) % mod);
}
