// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

#include <stdlib.h>

static int* bfs3820(int start, int n, int** g, int* deg) {
    const int inf = 1000000000;
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = inf;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    dist[start] = 0;
    q[qt++] = start;
    while (qh < qt) {
        int u = q[qh++];
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (dist[v] > dist[u] + 1) {
                dist[v] = dist[u] + 1;
                q[qt++] = v;
            }
        }
    }
    free(q);
    return dist;
}

int specialNodes(int n, int** edges, int edgesSize, int* edgesColSize, int x, int y, int z) {
    (void)edgesColSize;
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
    int* d1 = bfs3820(x, n, g, deg);
    int* d2 = bfs3820(y, n, g, deg);
    int* d3 = bfs3820(z, n, g, deg);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        long long a[3] = {d1[i], d2[i], d3[i]};
        if (a[0] > a[1]) { long long t=a[0]; a[0]=a[1]; a[1]=t; }
        if (a[1] > a[2]) { long long t=a[1]; a[1]=a[2]; a[2]=t; }
        if (a[0] > a[1]) { long long t=a[0]; a[0]=a[1]; a[1]=t; }
        if (a[0]*a[0] + a[1]*a[1] == a[2]*a[2]) ans++;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(d1); free(d2); free(d3);
    return ans;
}
