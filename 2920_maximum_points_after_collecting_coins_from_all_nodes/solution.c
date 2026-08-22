// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

#include <stdlib.h>
#include <string.h>

static int** g_g; static int* g_gsz; static int* g_coins; static int g_k;
static int* memo; static char* seen;
static int g_n;

static int dfs(int u, int p, int shifts) {
    if (shifts > 14) shifts = 14;
    int key = u * 15 + shifts;
    if (seen[key]) return memo[key];
    int c = g_coins[u] >> shifts;
    int opt1 = c - g_k;
    int opt2 = c / 2;
    for (int i = 0; i < g_gsz[u]; i++) {
        int v = g_g[u][i];
        if (v == p) continue;
        opt1 += dfs(v, u, shifts);
        opt2 += dfs(v, u, shifts + 1);
    }
    int best = opt1 > opt2 ? opt1 : opt2;
    seen[key] = 1; memo[key] = best;
    return best;
}

int maximumPoints(int** edges, int edgesSize, int* edgesColSize, int* coins, int coinsSize, int k) {
    (void)edgesColSize;
    int n = coinsSize;
    g_n = n; g_coins = coins; g_k = k;
    g_g = (int**)calloc(n, sizeof(int*));
    g_gsz = (int*)calloc(n, sizeof(int));
    int* gcap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (g_gsz[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 4; g_g[u] = (int*)realloc(g_g[u], gcap[u]*sizeof(int)); }
        g_g[u][g_gsz[u]++] = v;
        if (g_gsz[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 4; g_g[v] = (int*)realloc(g_g[v], gcap[v]*sizeof(int)); }
        g_g[v][g_gsz[v]++] = u;
    }
    memo = (int*)calloc(n * 15, sizeof(int));
    seen = (char*)calloc(n * 15, 1);
    int ans = dfs(0, -1, 0);
    for (int i = 0; i < n; i++) free(g_g[i]);
    free(g_g); free(g_gsz); free(gcap); free(memo); free(seen);
    return ans;
}
