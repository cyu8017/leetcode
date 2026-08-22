// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int reachableNodes(int n, int** edges, int edgesSize, int* edgesColSize, int* restricted, int restrictedSize) {
    (void)edgesColSize;
    bool* ban = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < restrictedSize; i++) ban[restricted[i]] = true;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gs = (int*)calloc((size_t)n, sizeof(int));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (gs[a] == gc[a]) { gc[a] = gc[a] ? gc[a]*2 : 2; g[a] = (int*)realloc(g[a], (size_t)gc[a]*sizeof(int)); }
        if (gs[b] == gc[b]) { gc[b] = gc[b] ? gc[b]*2 : 2; g[b] = (int*)realloc(g[b], (size_t)gc[b]*sizeof(int)); }
        g[a][gs[a]++] = b; g[b][gs[b]++] = a;
    }
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = 0; vis[0] = true;
    int ans = 0;
    while (qh < qt) {
        int u = q[qh++]; ans++;
        for (int i = 0; i < gs[u]; i++) {
            int v = g[u][i];
            if (!vis[v] && !ban[v]) { vis[v] = true; q[qt++] = v; }
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gs); free(gc); free(ban); free(vis); free(q);
    return ans;
}
