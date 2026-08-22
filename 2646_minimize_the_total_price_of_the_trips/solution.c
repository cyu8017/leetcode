// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

#include <stdlib.h>
#include <string.h>

static int min2646(int a, int b) { return a < b ? a : b; }

static int path2646(int** g, int* gSz, int* cnt, int u, int p, int target) {
    if (u == target) { cnt[u]++; return 1; }
    for (int i = 0; i < gSz[u]; i++) {
        int v = g[u][i];
        if (v == p) continue;
        if (path2646(g, gSz, cnt, v, u, target)) { cnt[u]++; return 1; }
    }
    return 0;
}

static void dfs2646(int** g, int* gSz, int* price, int* cnt, int u, int p, int* fullOut, int* halfOut) {
    int full = price[u] * cnt[u];
    int half = full / 2;
    for (int i = 0; i < gSz[u]; i++) {
        int v = g[u][i];
        if (v == p) continue;
        int nf, hf;
        dfs2646(g, gSz, price, cnt, v, u, &nf, &hf);
        full += min2646(nf, hf);
        half += nf;
    }
    *fullOut = full;
    *halfOut = half;
}

int minimumTotalPrice(int n, int** edges, int edgesSize, int* edgesColSize, int* price, int priceSize, int** trips, int tripsSize, int* tripsColSize) {
    (void)edgesColSize; (void)priceSize; (void)tripsColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    int* gSz = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int t = 0; t < 2; t++) {
            int a = t ? v : u, b = t ? u : v;
            if (gSz[a] == gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 4;
                g[a] = (int*)realloc(g[a], (size_t)gCap[a] * sizeof(int));
            }
            g[a][gSz[a]++] = b;
        }
    }
    int* cnt = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < tripsSize; i++)
        path2646(g, gSz, cnt, trips[i][0], -1, trips[i][1]);
    int a, b;
    dfs2646(g, gSz, price, cnt, 0, -1, &a, &b);
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gCap); free(gSz); free(cnt);
    return min2646(a, b);
}
