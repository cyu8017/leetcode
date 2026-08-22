// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int maxStarSum(int* vals, int valsSize, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    int n = valsSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        for (int t = 0; t < 2; t++) {
            int u = t ? b : a, v = t ? a : b;
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                g[u] = (int*)realloc(g[u], (size_t)cap[u] * sizeof(int));
            }
            g[u][deg[u]++] = v;
        }
    }
    int ans = vals[0];
    int* neigh = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int nc = 0;
        for (int j = 0; j < deg[i]; j++) {
            if (vals[g[i][j]] > 0) neigh[nc++] = vals[g[i][j]];
        }
        qsort(neigh, (size_t)nc, sizeof(int), cmp_desc);
        int sum = vals[i];
        for (int j = 0; j < nc && j < k; j++) sum += neigh[j];
        if (sum > ans) ans = sum;
    }
    free(neigh);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap);
    return ans;
}
