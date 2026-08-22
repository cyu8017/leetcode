// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MOD 1000000007
#define MAXM 1024

static int g_ans;
static int** g;
static int* gSize;
static int* g_vals;

static bool digitMask(int x, int* maskOut, int* vOut) {
    int mask = 0, v = x;
    if (x == 0) { *maskOut = 1; *vOut = 0; return true; }
    while (x > 0) {
        int d = x % 10;
        if (mask & (1 << d)) return false;
        mask |= 1 << d;
        x /= 10;
    }
    *maskOut = mask; *vOut = v;
    return true;
}

static void dfs(int u, int* dp) {
    memset(dp, 0x80, MAXM * sizeof(int)); /* -big */
    dp[0] = 0;
    int mask, v;
    if (digitMask(g_vals[u], &mask, &v)) {
        if (v > dp[mask]) dp[mask] = v;
    }
    int* ndp = (int*)malloc(MAXM * sizeof(int));
    int* child = (int*)malloc(MAXM * sizeof(int));
    for (int ci = 0; ci < gSize[u]; ci++) {
        dfs(g[u][ci], child);
        memset(ndp, 0x80, MAXM * sizeof(int));
        for (int m1 = 0; m1 < MAXM; m1++) {
            if (dp[m1] < -1000000000) continue;
            for (int m2 = 0; m2 < MAXM; m2++) {
                if (child[m2] < -1000000000) continue;
                if ((m1 & m2) == 0) {
                    int nm = m1 | m2;
                    int s = dp[m1] + child[m2];
                    if (s > ndp[nm]) ndp[nm] = s;
                }
            }
        }
        for (int m = 0; m < MAXM; m++) {
            if (dp[m] > ndp[m]) ndp[m] = dp[m];
            if (child[m] > ndp[m]) ndp[m] = child[m];
        }
        memcpy(dp, ndp, MAXM * sizeof(int));
    }
    free(ndp); free(child);
    int best = 0;
    for (int m = 0; m < MAXM; m++) if (dp[m] > best) best = dp[m];
    g_ans = (g_ans + best) % MOD;
}

int goodSubtreeSum(int* vals, int valsSize, int* par, int parSize) {
    (void)parSize;
    int n = valsSize;
    g_vals = vals; g_ans = 0;
    g = (int**)calloc((size_t)n, sizeof(int*));
    gSize = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int p = par[i];
        if (gSize[p] == gCap[p]) {
            gCap[p] = gCap[p] ? gCap[p] * 2 : 4;
            g[p] = (int*)realloc(g[p], (size_t)gCap[p] * sizeof(int));
        }
        g[p][gSize[p]++] = i;
    }
    int* dp = (int*)malloc(MAXM * sizeof(int));
    dfs(0, dp);
    free(dp);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gSize); free(gCap);
    return g_ans;
}
