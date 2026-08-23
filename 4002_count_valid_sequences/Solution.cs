// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

public class Solution {
    const int MX = 500001;
    const long MOD = 1000000007L;
    static long[] f = new long[MX];
    static long[] g = new long[MX];
    static bool inited;

    static long ModPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    static void EnsureInit() {
        if (inited) return;
        inited = true;
        f[0] = 1;
        g[0] = 1;
        for (int i = 1; i < MX; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = ModPow(f[i], MOD - 2);
        }
    }

    static long Comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return f[n] * g[k] % MOD * g[n - k] % MOD;
    }

    public int CountValidSequences(int n, int k) {
        EnsureInit();
        long ans = Comb(n - 1, k - 1);
        if ((n + k) % 2 == 0) {
            ans = (ans - Comb((n + k) / 2 - 1, k - 1) + MOD) % MOD;
        }
        return (int)ans;
    }
}
