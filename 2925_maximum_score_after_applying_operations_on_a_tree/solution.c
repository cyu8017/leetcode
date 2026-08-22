// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

#include <stdlib.h>

static long long dfs(int** g, int* gsz, int* values, int u, int p) {
    long long sumKids = 0;
    int isLeaf = 1;
    for (int i = 0; i < gsz[u]; i++) {
        int v = g[u][i];
        if (v == p) continue;
        isLeaf = 0;
        sumKids += dfs(g, gsz, values, v, u);
    }
    if (isLeaf) return values[u];
    return values[u] < sumKids ? values[u] : sumKids;
}

long long maximumScoreAfterOperations(int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize) {
    (void)edgesColSize;
    int n = valuesSize;
    int** g = (int**)calloc(n, sizeof(int*));
    int* gsz = (int*)calloc(n, sizeof(int));
    int* gcap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gsz[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 4; g[u] = (int*)realloc(g[u], gcap[u]*sizeof(int)); }
        g[u][gsz[u]++] = v;
        if (gsz[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 4; g[v] = (int*)realloc(g[v], gcap[v]*sizeof(int)); }
        g[v][gsz[v]++] = u;
    }
    long long total = 0;
    for (int i = 0; i < n; i++) total += values[i];
    long long ans = total - dfs(g, gsz, values, 0, -1);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap);
    return ans;
}
