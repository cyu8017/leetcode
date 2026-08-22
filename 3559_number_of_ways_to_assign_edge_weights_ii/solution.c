// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

#include <stdlib.h>
#include <string.h>

#define LOG 17
#define MOD 1000000007

static int mod_pow(int exp) {
    long long base = 2, res = 1;
    while (exp > 0) {
        if (exp & 1) res = res * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    return (int)res;
}

static void dfs(int u, int p, int** graph, int* gSize, int* depth, int parent[][LOG + 1]) {
    parent[u][0] = p;
    for (int i = 0; i < gSize[u]; i++) {
        int v = graph[u][i];
        if (v != p) {
            depth[v] = depth[u] + 1;
            dfs(v, u, graph, gSize, depth, parent);
        }
    }
}

static int lca(int u, int v, int* depth, int parent[][LOG + 1]) {
    if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
    for (int k = LOG - 1; k >= 0; k--) {
        if (parent[u][k] != -1 && depth[parent[u][k]] >= depth[v]) u = parent[u][k];
    }
    if (u == v) return u;
    for (int k = LOG - 1; k >= 0; k--) {
        if (parent[u][k] != -1 && parent[u][k] != parent[v][k]) {
            u = parent[u][k];
            v = parent[v][k];
        }
    }
    return parent[u][0];
}

int* assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgesColSize; (void)queriesColSize;
    int n = edgesSize + 1;
    int** graph = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int* gSize = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* gCap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int r = 0; r < 2; r++) {
            int a = r ? v : u, b = r ? u : v;
            if (gSize[a] == gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 4;
                graph[a] = (int*)realloc(graph[a], (size_t)gCap[a] * sizeof(int));
            }
            graph[a][gSize[a]++] = b;
        }
    }
    int* depth = (int*)calloc((size_t)(n + 1), sizeof(int));
    static int parent[100005][LOG + 1];
    for (int i = 0; i <= n; i++) for (int k = 0; k < LOG; k++) parent[i][k] = -1;
    dfs(1, -1, graph, gSize, depth, parent);
    for (int k = 1; k < LOG; k++) {
        for (int v = 1; v <= n; v++) {
            if (parent[v][k - 1] != -1) parent[v][k] = parent[parent[v][k - 1]][k - 1];
        }
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int u = queries[i][0], v = queries[i][1];
        if (u == v) { ans[i] = 0; continue; }
        int a = lca(u, v, depth, parent);
        int d = depth[u] + depth[v] - 2 * depth[a];
        ans[i] = mod_pow(d - 1);
    }
    *returnSize = queriesSize;
    for (int i = 0; i <= n; i++) free(graph[i]);
    free(graph); free(gSize); free(gCap); free(depth);
    return ans;
}
