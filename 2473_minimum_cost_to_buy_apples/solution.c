// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

#include <stdlib.h>
#include <string.h>

typedef struct { int to, w; } Edge2473;
typedef struct { int node; long long dist; } Item2473;

static void push2473(Item2473* h, int* n, Item2473 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].dist <= h[i].dist) break;
        Item2473 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static Item2473 pop2473(Item2473* h, int* n) {
    Item2473 res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && h[l].dist < h[best].dist) best = l;
        if (r < *n && h[r].dist < h[best].dist) best = r;
        if (best == i) break;
        Item2473 t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

long long* minCost(int n, int** roads, int roadsSize, int* roadsColSize, int* appleCost, int appleCostSize, int k, int* returnSize) {
    (void)roadsColSize; (void)appleCostSize;
    Edge2473** g = (Edge2473**)calloc((size_t)(n + 1), sizeof(Edge2473*));
    int* deg = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* cap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        int a = roads[i][0], b = roads[i][1], w = roads[i][2];
        for (int t = 0; t < 2; t++) {
            int u = t ? b : a, v = t ? a : b;
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                g[u] = (Edge2473*)realloc(g[u], (size_t)cap[u] * sizeof(Edge2473));
            }
            g[u][deg[u]++] = (Edge2473){v, w};
        }
    }
    long long* ans = (long long*)malloc((size_t)n * sizeof(long long));
    long long INF = 1LL << 60;
    long long* dist = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    Item2473* heap = (Item2473*)malloc((size_t)(roadsSize * 4 + n + 5) * sizeof(Item2473));
    for (int start = 1; start <= n; start++) {
        for (int i = 0; i <= n; i++) dist[i] = INF;
        dist[start] = 0;
        int hn = 0;
        push2473(heap, &hn, (Item2473){start, 0});
        while (hn > 0) {
            Item2473 cur = pop2473(heap, &hn);
            if (cur.dist != dist[cur.node]) continue;
            for (int i = 0; i < deg[cur.node]; i++) {
                Edge2473 e = g[cur.node][i];
                long long nd = cur.dist + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    push2473(heap, &hn, (Item2473){e.to, nd});
                }
            }
        }
        long long best = INF;
        for (int city = 1; city <= n; city++) {
            long long cost = dist[city] * (k + 1) + appleCost[city - 1];
            if (cost < best) best = cost;
        }
        ans[start - 1] = best;
    }
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(dist); free(heap);
    *returnSize = n;
    return ans;
}
