// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

#include <stdlib.h>
#include <string.h>

static int bits_count(int x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}

int maximumCost(int n, int** highways, int highwaysSize, int* highwaysColSize, int k) {
    (void)highwaysColSize;
    if (k + 1 > n) return -1;
    int** to = (int**)calloc((size_t)n, sizeof(int*));
    int** w = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < highwaysSize; i++) {
        int a = highways[i][0], b = highways[i][1], cost = highways[i][2];
        for (int pass = 0; pass < 2; pass++) {
            int u = pass ? b : a, v = pass ? a : b;
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                to[u] = (int*)realloc(to[u], (size_t)cap[u] * sizeof(int));
                w[u] = (int*)realloc(w[u], (size_t)cap[u] * sizeof(int));
            }
            to[u][deg[u]] = v;
            w[u][deg[u]] = cost;
            deg[u]++;
        }
    }
    int masks = 1 << n;
    int** dp = (int**)malloc((size_t)masks * sizeof(int*));
    for (int i = 0; i < masks; i++) {
        dp[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dp[i][j] = -1;
    }
    for (int i = 0; i < n; i++) dp[1 << i][i] = 0;
    int ans = -1;
    for (int mask = 0; mask < masks; mask++) {
        int cities = bits_count(mask);
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] < 0) continue;
            if (cities - 1 == k && dp[mask][u] > ans) ans = dp[mask][u];
            for (int e = 0; e < deg[u]; e++) {
                int v = to[u][e];
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                int cand = dp[mask][u] + w[u][e];
                if (cand > dp[nm][v]) dp[nm][v] = cand;
            }
        }
    }
    for (int i = 0; i < masks; i++) free(dp[i]);
    free(dp);
    for (int i = 0; i < n; i++) { free(to[i]); free(w[i]); }
    free(to); free(w); free(deg); free(cap);
    return ans;
}
