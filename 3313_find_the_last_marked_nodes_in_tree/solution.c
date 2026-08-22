// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

#include <stdlib.h>

static int bfs3313(int start, int** g, int* glen, int n, int* dist) {
    for (int i = 0; i < n; i++) dist[i] = -1;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = start; dist[start] = 0;
    int far = start;
    while (qh < qt) {
        int u = q[qh++];
        if (dist[u] > dist[far]) far = u;
        for (int i = 0; i < glen[u]; i++) {
            int v = g[u][i];
            if (dist[v] == -1) { dist[v] = dist[u] + 1; q[qt++] = v; }
        }
    }
    free(q);
    return far;
}

int* lastMarkedNodes(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (glen[a] == gcap[a]) { gcap[a] *= 2; g[a] = realloc(g[a], (size_t)gcap[a] * sizeof(int)); }
        if (glen[b] == gcap[b]) { gcap[b] *= 2; g[b] = realloc(g[b], (size_t)gcap[b] * sizeof(int)); }
        g[a][glen[a]++] = b; g[b][glen[b]++] = a;
    }
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    int u = bfs3313(0, g, glen, n, dist);
    int* du = (int*)malloc((size_t)n * sizeof(int));
    int v = bfs3313(u, g, glen, n, du);
    int* dv = (int*)malloc((size_t)n * sizeof(int));
    bfs3313(v, g, glen, n, dv);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = (du[i] >= dv[i]) ? u : v;
    *returnSize = n;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap); free(dist); free(du); free(dv);
    return ans;
}
