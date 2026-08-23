// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

#include <vector>

class Solution {
    static const int N = 31;
    static const int MOD = 1000000007;
    long long f[N], g[N];
    bool inited = false;
    long long qpow(long long a, long long k) {
        long long res = 1;
        while (k > 0) {
            if (k & 1) res = res * a % MOD;
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
    long long comb(int m, int n) {
        if (n < 0 || n > m) return 0;
        return f[m] * g[n] % MOD * g[m - n] % MOD;
    }
public:
    int magicalSum(int m, int k, std::vector<int>& nums) {
        initFact();
        int n = (int)nums.size();
        std::vector dp(n + 1, std::vector(m + 1, std::vector(k + 1, std::vector<long long>(N, -1))));
        auto dfs = [&](auto&& self, int i, int j, int kk, int st) -> long long {
            if (kk < 0 || (i == n && j > 0)) return 0;
            if (i == n) {
                while (st > 0) { kk -= st & 1; st >>= 1; }
                return kk == 0 ? 1 : 0;
            }
            if (dp[i][j][kk][st] != -1) return dp[i][j][kk][st];
            long long res = 0;
            for (int t = 0; t <= j; t++) {
                int nt = t + st;
                int nk = kk - (nt & 1);
                long long p = qpow(nums[i], t);
                long long tmp = comb(j, t) * p % MOD * self(self, i + 1, j - t, nk, nt >> 1) % MOD;
                res = (res + tmp) % MOD;
            }
            return dp[i][j][kk][st] = res;
        };
        return (int)dfs(dfs, 0, m, k, 0);
    }
};
