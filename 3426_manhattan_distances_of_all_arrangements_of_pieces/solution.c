// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

static int modPow3426(long long a, long long e, int mod) {
    long long r = 1; while (e > 0) { if (e & 1) r = r * a % mod; a = a * a % mod; e >>= 1; } return (int)r;
}
static int comb3426(int n, int k, int mod) {
    if (k < 0 || k > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < k; i++) { num = num * (n - i) % mod; den = den * (i + 1) % mod; }
    return (int)(num * modPow3426(den, mod - 2, mod) % mod);
}
int distanceSum(int m, int n, int k) {
    const int mod = 1000000007;
    if (k < 2) return 0;
    int pairChoose = comb3426(m * n - 2, k - 2, mod);
    long long sumDist = 0;
    for (int d = 1; d < m; d++) sumDist += (long long)d * (m - d) * n * n;
    for (int d = 1; d < n; d++) sumDist += (long long)d * (n - d) * m * m;
    return (int)(sumDist % mod * pairChoose % mod);
}
