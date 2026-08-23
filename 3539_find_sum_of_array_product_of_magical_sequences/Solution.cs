// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

public class Solution {
    const int N = 31;
    const int MOD = 1000000007;
    long[] f = new long[N], g = new long[N];
    bool inited = false;
    long Qpow(long a, long k) {
        long res = 1;
        while (k > 0) {
            if ((k & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            k >>= 1;
        }
        return res;
    }
    void InitFact() {
        if (inited) return;
        f[0] = g[0] = 1;
        for (int i = 1; i < N; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = Qpow(f[i], MOD - 2);
        }
        inited = true;
    }
    long Comb(int m, int n) {
        if (n < 0 || n > m) return 0;
        return f[m] * g[n] % MOD * g[m - n] % MOD;
    }
    public int MagicalSum(int m, int k, int[] nums) {
        InitFact();
        int n = nums.Length;
        long[][][][] dp = new long[n + 1][][][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new long[m + 1][][];
            for (int j = 0; j <= m; j++) {
                dp[i][j] = new long[k + 1][];
                for (int kk = 0; kk <= k; kk++) {
                    dp[i][j][kk] = new long[N];
                    for (int s = 0; s < N; s++) dp[i][j][kk][s] = -1;
                }
            }
        }
        long Dfs(int i, int j, int kk, int st) {
            if (kk < 0 || (i == n && j > 0)) return 0;
            if (i == n) {
                while (st > 0) { kk -= st & 1; st >>= 1; }
                return kk == 0 ? 1 : 0;
            }
            if (dp[i][j][kk][st] != -1) return dp[i][j][kk][st];
            long res = 0;
            for (int t = 0; t <= j; t++) {
                int nt = t + st;
                int nk = kk - (nt & 1);
                long p = Qpow(nums[i], t);
                long tmp = Comb(j, t) * p % MOD * Dfs(i + 1, j - t, nk, nt >> 1) % MOD;
                res = (res + tmp) % MOD;
            }
            return dp[i][j][kk][st] = res;
        }
        return (int)Dfs(0, m, k, 0);
    }
}
