// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int cmp_edge(const void* a, const void* b) {
    int* const* ea = (int* const*)a;
    int* const* eb = (int* const*)b;
    return (*ea)[2] - (*eb)[2];
}

static bool check3807(int n, int** edges, int idx, int k) {
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i <= idx; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u]*2 : 4; g[u] = (int*)realloc(g[u], (size_t)cap[u]*sizeof(int)); }
        g[u][deg[u]++] = v;
        if (deg[v] == cap[v]) { cap[v] = cap[v] ? cap[v]*2 : 4; g[v] = (int*)realloc(g[v], (size_t)cap[v]*sizeof(int)); }
        g[v][deg[v]++] = u;
    }
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    q[qt++] = 0; vis[0] = true;
    int dist = 0;
    bool ok = false;
    while (qh < qt) {
        int sz = qt - qh;
        for (int s = 0; s < sz; s++) {
            int u = q[qh++];
            if (u == n - 1) { ok = dist <= k; goto done; }
            for (int j = 0; j < deg[u]; j++) {
                int v = g[u][j];
                if (!vis[v]) { vis[v] = true; q[qt++] = v; }
            }
        }
        dist++;
    }
done:
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(q); free(vis);
    return ok;
}

int minCost(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    qsort(edges, (size_t)edgesSize, sizeof(int*), cmp_edge);
    int m = edgesSize;
    int l = 0, r = m - 1;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (check3807(n, edges, mid, k)) r = mid;
        else l = mid + 1;
    }
    if (check3807(n, edges, l, k)) return edges[l][2];
    return -1;
}
