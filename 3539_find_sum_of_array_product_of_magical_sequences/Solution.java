// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

class Solution {
    static final int N = 31;
    static final int MOD = 1_000_000_007;
    long[] f = new long[N], g = new long[N];
    boolean inited = false;
    long[][][][] dp;
    int[] nums;
    int n;

    long qpow(long a, long k) {
        long res = 1;
        while (k > 0) {
            if ((k & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            k >>= 1;
        }
        return res;
    }

    void initFact() {
        if (inited) return;
        f[0] = g[0] = 1;
        for (int i = 1; i < N; i++) {
            f[i] = f[i - 1] * i % MOD;
            g[i] = qpow(f[i], MOD - 2);
        }
        inited = true;
    }

    long comb(int m, int nn) {
        if (nn < 0 || nn > m) return 0;
        return f[m] * g[nn] % MOD * g[m - nn] % MOD;
    }

    long dfs(int i, int j, int kk, int st) {
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
            long p = qpow(nums[i], t);
            long tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD;
            res = (res + tmp) % MOD;
        }
        return dp[i][j][kk][st] = res;
    }

    public int magicalSum(int m, int k, int[] nums) {
        initFact();
        this.nums = nums;
        n = nums.length;
        dp = new long[n + 1][m + 1][k + 1][N];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= m; j++)
                for (int kk = 0; kk <= k; kk++)
                    java.util.Arrays.fill(dp[i][j][kk], -1);
        return (int) dfs(0, m, k, 0);
    }
}
