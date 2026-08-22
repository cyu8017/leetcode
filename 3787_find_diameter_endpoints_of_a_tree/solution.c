// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

#include <stdlib.h>
#include <string.h>

static int bfs3787(int start, int n, int** g, int* deg, int* dist) {
    for (int i = 0; i < n; i++) dist[i] = -1;
    dist[start] = 0;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = start;
    int far = start;
    while (qh < qt) {
        int u = q[qh++];
        if (dist[u] > dist[far]) far = u;
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j];
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q[qt++] = v;
            }
        }
    }
    free(q);
    return far;
}

char* findSpecialNodes(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a]*2 : 4; g[a] = (int*)realloc(g[a], (size_t)cap[a]*sizeof(int)); }
        g[a][deg[a]++] = b;
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b]*2 : 4; g[b] = (int*)realloc(g[b], (size_t)cap[b]*sizeof(int)); }
        g[b][deg[b]++] = a;
    }
    int* dist1 = (int*)malloc((size_t)n * sizeof(int));
    int* dist2 = (int*)malloc((size_t)n * sizeof(int));
    int a = bfs3787(0, n, g, deg, dist1);
    int b = bfs3787(a, n, g, deg, dist1);
    bfs3787(b, n, g, deg, dist2);
    int d = dist1[b];
    char* ans = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        ans[i] = (dist1[i] == d || dist2[i] == d) ? '1' : '0';
    }
    ans[n] = '\0';
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(dist1); free(dist2);
    return ans;
}
