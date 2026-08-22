// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

#include <stdlib.h>

long long interactionCost(int n, int** edges, int edgesSize, int* edgesColSize, int* group, int groupSize) {
    (void)edgesColSize; (void)groupSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u]*2 : 4; g[u] = (int*)realloc(g[u], (size_t)cap[u]*sizeof(int)); }
        g[u][deg[u]++] = v;
        if (deg[v] == cap[v]) { cap[v] = cap[v] ? cap[v]*2 : 4; g[v] = (int*)realloc(g[v], (size_t)cap[v]*sizeof(int)); }
        g[v][deg[v]++] = u;
    }
    int total[21] = {0};
    for (int i = 0; i < n; i++) total[group[i]]++;
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
            if (parent[v] == -2) { parent[v] = u; order[osz++] = v; }
        }
    }
    int (*count)[21] = calloc((size_t)n, sizeof(*count));
    long long ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        count[u][group[u]]++;
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (parent[v] != u) continue;
            for (int c = 1; c <= 20; c++) {
                int x = count[v][c];
                ans += (long long)x * (total[c] - x);
                count[u][c] += x;
            }
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(parent); free(order); free(count);
    return ans;
}
