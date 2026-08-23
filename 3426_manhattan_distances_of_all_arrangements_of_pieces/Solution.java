// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

class Solution {
    private static long modPow(long a, long e, int mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }

    private static int comb(int n, int k, int mod) {
        if (k < 0 || k > n) return 0;
        long num = 1, den = 1;
        for (int i = 0; i < k; i++) {
            num = num * (n - i) % mod;
            den = den * (i + 1) % mod;
        }
        return (int) (num * modPow(den, mod - 2, mod) % mod);
    }

    public int distanceSum(int m, int n, int k) {
        final int mod = 1_000_000_007;
        if (k < 2) return 0;
        int totalCells = m * n;
        int pairChoose = comb(totalCells - 2, k - 2, mod);
        long sumDist = 0;
        for (int d = 1; d < m; d++) sumDist += (long) d * (m - d) * n * n;
        for (int d = 1; d < n; d++) sumDist += (long) d * (n - d) * m * m;
        return (int) (sumDist % mod * pairChoose % mod);
    }
}
