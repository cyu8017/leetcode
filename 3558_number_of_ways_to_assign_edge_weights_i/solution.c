// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

#include <stdlib.h>
#include <string.h>

static int mod_pow(long long a, int n, int mod) {
    long long res = 1;
    a %= mod;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return (int)res;
}

static int dfs_depth(int i, int fa, int** g, int* gSize) {
    int res = 0;
    for (int t = 0; t < gSize[i]; t++) {
        int j = g[i][t];
        if (j != fa) {
            int d = dfs_depth(j, i, g, gSize) + 1;
            if (d > res) res = d;
        }
    }
    return res;
}

int assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    const int mod = 1000000007;
    int n = edgesSize + 1;
    int** g = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int* gSize = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* gCap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int rep = 0; rep < 2; rep++) {
            int a = rep ? v : u, b = rep ? u : v;
            if (gSize[a] == gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 4;
                g[a] = (int*)realloc(g[a], (size_t)gCap[a] * sizeof(int));
            }
            g[a][gSize[a]++] = b;
        }
    }
    int depth = dfs_depth(1, 0, g, gSize);
    int ans = mod_pow(2, depth - 1, mod);
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g); free(gSize); free(gCap);
    return ans;
}
