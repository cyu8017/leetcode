// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

class Solution {
    private static final int MX = 500001;
    private static final long MOD = 1000000007L;
    private static final long[] f = new long[MX];
    private static final long[] g = new long[MX];
    private static boolean inited = false;

    private static long modPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    private static void ensureInit() {
        if (inited) return;
        inited = true;
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i < MX; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = modPow(f[i], MOD - 2);
        }
    }

    private static long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return f[n] * g[k] % MOD * g[n - k] % MOD;
    }

    public int countValidSequences(int n, int k) {
        ensureInit();
        long ans = comb(n - 1, k - 1);
        if ((n + k) % 2 == 0) {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        return (int) ans;
    }
}
