// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

static int modPow(long long a, int e, int mod) {
    long long res = 1; a %= mod;
    while (e > 0) {
        if (e & 1) res = res * a % mod;
        a = a * a % mod; e >>= 1;
    }
    return (int)res;
}

static int comb(int n, int r, int mod) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; i++) {
        num = num * (n - i) % mod;
        den = den * (i + 1) % mod;
    }
    return (int)(num * modPow(den, mod - 2, mod) % mod);
}

int numberOfWays(int startPos, int endPos, int k) {
    const int mod = 1000000007;
    int diff = endPos - startPos;
    if (diff < 0) diff = -diff;
    if (diff > k || (k - diff) % 2 != 0) return 0;
    return comb(k, (k + diff) / 2, mod);
}
