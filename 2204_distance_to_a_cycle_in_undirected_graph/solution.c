// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

#include <stdlib.h>
#include <stdbool.h>

int* distanceToCycle(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gLen = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gLen[u] == gCap[u]) { gCap[u] = gCap[u] ? gCap[u]*2 : 4; g[u] = realloc(g[u], (size_t)gCap[u]*sizeof(int)); }
        if (gLen[v] == gCap[v]) { gCap[v] = gCap[v] ? gCap[v]*2 : 4; g[v] = realloc(g[v], (size_t)gCap[v]*sizeof(int)); }
        g[u][gLen[u]++] = v; g[v][gLen[v]++] = u;
        deg[u]++; deg[v]++;
    }
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; i++) if (deg[i] == 1) q[qt++] = i;
    bool* onCycle = (bool*)malloc((size_t)n * sizeof(bool));
    for (int i = 0; i < n; i++) onCycle[i] = true;
    while (qh < qt) {
        int u = q[qh++];
        onCycle[u] = false;
        for (int t = 0; t < gLen[u]; t++) {
            int v = g[u][t];
            if (--deg[v] == 1) q[qt++] = v;
        }
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = -1;
    qh = qt = 0;
    for (int i = 0; i < n; i++) if (onCycle[i]) { ans[i] = 0; q[qt++] = i; }
    while (qh < qt) {
        int u = q[qh++];
        for (int t = 0; t < gLen[u]; t++) {
            int v = g[u][t];
            if (ans[v] == -1) { ans[v] = ans[u] + 1; q[qt++] = v; }
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gLen); free(gCap); free(deg); free(q); free(onCycle);
    *returnSize = n;
    return ans;
}
