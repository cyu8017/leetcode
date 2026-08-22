// LeetCode 3367 - Maximize Sum of Weights After Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

#include <stdlib.h>

typedef struct { int to, w; } E3367;
typedef struct { E3367* a; int n, cap; } Adj3367;

static void adj_push(Adj3367* g, int u, int to, int w) {
    if (g[u].n == g[u].cap) {
        g[u].cap = g[u].cap ? g[u].cap * 2 : 4;
        g[u].a = (E3367*)realloc(g[u].a, g[u].cap * sizeof(E3367));
    }
    g[u].a[g[u].n++] = (E3367){to, w};
}

static int cmp_ll_desc(const void* a, const void* b) {
    long long x = *(const long long*)a, y = *(const long long*)b;
    return (x < y) - (x > y);
}

static Adj3367* G3367;
static int K3367;

static void dfs3367(int u, int p, long long* with, long long* without) {
    long long base = 0;
    long long* gains = NULL; int gn = 0, gcap = 0;
    for (int i = 0; i < G3367[u].n; i++) {
        int v = G3367[u].a[i].to, w = G3367[u].a[i].w;
        if (v == p) continue;
        long long keep, drop;
        dfs3367(v, u, &keep, &drop);
        base += drop;
        long long gain = keep + w - drop;
        if (gain > 0) {
            if (gn == gcap) { gcap = gcap ? gcap * 2 : 4; gains = (long long*)realloc(gains, gcap * sizeof(long long)); }
            gains[gn++] = gain;
        }
    }
    qsort(gains, gn, sizeof(long long), cmp_ll_desc);
    long long wi = base, wo = base;
    for (int i = 0; i < gn && i < K3367 - 1; i++) wi += gains[i];
    for (int i = 0; i < gn && i < K3367; i++) wo += gains[i];
    *with = wi; *without = wo;
    free(gains);
}

long long maximizeSumOfWeights(int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    int n = edgesSize + 1;
    G3367 = (Adj3367*)calloc(n, sizeof(Adj3367));
    K3367 = k;
    for (int i = 0; i < edgesSize; i++) {
        adj_push(G3367, edges[i][0], edges[i][1], edges[i][2]);
        adj_push(G3367, edges[i][1], edges[i][0], edges[i][2]);
    }
    long long with, without;
    dfs3367(0, -1, &with, &without);
    for (int i = 0; i < n; i++) free(G3367[i].a);
    free(G3367);
    return without;
}
