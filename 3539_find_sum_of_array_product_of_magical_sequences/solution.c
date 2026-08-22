// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

#include <stdlib.h>
#include <string.h>

#define N3539 31
#define MOD3539 1000000007

static long long f3539[N3539], g3539[N3539];
static int inited3539 = 0;

static long long qpow3539(long long a, long long k) {
    long long res = 1;
    while (k > 0) {
        if (k & 1) res = res * a % MOD3539;
        a = a * a % MOD3539;
        k >>= 1;
    }
    return res;
}

static void init3539(void) {
    if (inited3539) return;
    f3539[0] = g3539[0] = 1;
    for (int i = 1; i < N3539; i++) {
        f3539[i] = f3539[i - 1] * i % MOD3539;
        g3539[i] = qpow3539(f3539[i], MOD3539 - 2);
    }
    inited3539 = 1;
}

static long long comb3539(int m, int n) {
    if (n < 0 || n > m) return 0;
    return f3539[m] * g3539[n] % MOD3539 * g3539[m - n] % MOD3539;
}

static int n3539a, m3539, k3539;
static int* nums3539;
static long long**** dp3539;

static long long dfs3539(int i, int j, int kk, int st) {
    if (kk < 0 || (i == n3539a && j > 0)) return 0;
    if (i == n3539a) {
        while (st > 0) { kk -= st & 1; st >>= 1; }
        return kk == 0 ? 1 : 0;
    }
    if (dp3539[i][j][kk][st] != -1) return dp3539[i][j][kk][st];
    long long res = 0;
    for (int t = 0; t <= j; t++) {
        int nt = t + st;
        int nk = kk - (nt & 1);
        long long p = qpow3539(nums3539[i], t);
        long long tmp = comb3539(j, t) * p % MOD3539 * dfs3539(i + 1, j - t, nk, nt >> 1) % MOD3539;
        res = (res + tmp) % MOD3539;
    }
    dp3539[i][j][kk][st] = res;
    return res;
}

int magicalSum(int m, int k, int* nums, int numsSize) {
    init3539();
    n3539a = numsSize; m3539 = m; k3539 = k; nums3539 = nums;
    dp3539 = (long long****)malloc((size_t)(n3539a + 1) * sizeof(long long***));
    for (int i = 0; i <= n3539a; i++) {
        dp3539[i] = (long long***)malloc((size_t)(m + 1) * sizeof(long long**));
        for (int j = 0; j <= m; j++) {
            dp3539[i][j] = (long long**)malloc((size_t)(k + 1) * sizeof(long long*));
            for (int l = 0; l <= k; l++) {
                dp3539[i][j][l] = (long long*)malloc((size_t)N3539 * sizeof(long long));
                for (int s = 0; s < N3539; s++) dp3539[i][j][l][s] = -1;
            }
        }
    }
    int ans = (int)dfs3539(0, m, k, 0);
    for (int i = 0; i <= n3539a; i++) {
        for (int j = 0; j <= m; j++) {
            for (int l = 0; l <= k; l++) free(dp3539[i][j][l]);
            free(dp3539[i][j]);
        }
        free(dp3539[i]);
    }
    free(dp3539);
    return ans;
}
