// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int* a; int n, cap; } Adj;
static void adj_push(Adj* g, int u, int v) {
    if (g[u].n == g[u].cap) { g[u].cap = g[u].cap ? g[u].cap * 2 : 4; g[u].a = (int*)realloc(g[u].a, g[u].cap * sizeof(int)); }
    g[u].a[g[u].n++] = v;
}

static int g_n; static int** g_edges; static int g_esize;

static int ok3419(int mid) {
    Adj* g = (Adj*)calloc(g_n, sizeof(Adj));
    for (int i = 0; i < g_esize; i++) if (g_edges[i][2] <= mid) adj_push(g, g_edges[i][1], g_edges[i][0]);
    bool* vis = (bool*)calloc(g_n, 1);
    int* q = (int*)malloc(g_n * sizeof(int)); int qh = 0, qt = 0, cnt = 1;
    q[qt++] = 0; vis[0] = true;
    while (qh < qt) {
        int u = q[qh++];
        for (int i = 0; i < g[u].n; i++) {
            int v = g[u].a[i];
            if (!vis[v]) { vis[v] = true; cnt++; q[qt++] = v; }
        }
    }
    for (int i = 0; i < g_n; i++) free(g[i].a);
    free(g); free(vis); free(q);
    return cnt == g_n;
}

int minMaxWeight(int n, int** edges, int edgesSize, int* edgesColSize, int threshold) {
    (void)edgesColSize; (void)threshold;
    g_n = n; g_edges = edges; g_esize = edgesSize;
    int lo = 1, hi = 1000001, ans = -1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (ok3419(mid)) { ans = mid; hi = mid; } else lo = mid + 1;
    }
    return ans;
}
