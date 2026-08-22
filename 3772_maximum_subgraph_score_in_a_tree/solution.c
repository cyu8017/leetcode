// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

#include <stdlib.h>
#include <string.h>

int* maxSubgraphScore(int n, int** edges, int edgesSize, int* edgesColSize, int* good, int goodSize, int* returnSize) {
    (void)edgesColSize; (void)goodSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (deg[u] == cap[u]) {
            cap[u] = cap[u] ? cap[u] * 2 : 4;
            g[u] = (int*)realloc(g[u], (size_t)cap[u] * sizeof(int));
        }
        g[u][deg[u]++] = v;
        if (deg[v] == cap[v]) {
            cap[v] = cap[v] ? cap[v] * 2 : 4;
            g[v] = (int*)realloc(g[v], (size_t)cap[v] * sizeof(int));
        }
        g[v][deg[v]++] = u;
    }
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = -2;
    parent[0] = -1;
    int* order = (int*)malloc((size_t)n * sizeof(int));
    int osz = 0;
    order[osz++] = 0;
    for (int i = 0; i < osz; i++) {
        int u = order[i];
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (parent[v] == -2) {
                parent[v] = u;
                order[osz++] = v;
            }
        }
    }
    int* down = (int*)malloc((size_t)n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        down[u] = 2 * good[u] - 1;
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (parent[v] == u && down[v] > 0) down[u] += down[v];
        }
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    memcpy(ans, down, (size_t)n * sizeof(int));
    for (int i = 0; i < osz; i++) {
        int u = order[i];
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (parent[v] == u) {
                int outside = ans[u];
                if (down[v] > 0) outside -= down[v];
                ans[v] = down[v];
                if (outside > 0) ans[v] += outside;
            }
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(parent); free(order); free(down);
    *returnSize = n;
    return ans;
}
