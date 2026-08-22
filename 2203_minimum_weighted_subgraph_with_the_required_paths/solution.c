// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

#include <stdlib.h>
#include <limits.h>

typedef struct { long long dist; int node; } Item;
typedef struct { int* to; int* w; int len; int cap; } Adj;

static void adjAdd(Adj* g, int v, int w) {
    if (g->len == g->cap) {
        g->cap = g->cap ? g->cap * 2 : 4;
        g->to = (int*)realloc(g->to, (size_t)g->cap * sizeof(int));
        g->w = (int*)realloc(g->w, (size_t)g->cap * sizeof(int));
    }
    g->to[g->len] = v; g->w[g->len] = w; g->len++;
}

typedef struct { Item* a; int n; } PQ;
static void pqSwap(Item* a, int i, int j) { Item t = a[i]; a[i] = a[j]; a[j] = t; }
static void pqUp(PQ* p, int i) {
    while (i > 0) {
        int par = (i - 1) / 2;
        if (p->a[i].dist >= p->a[par].dist) break;
        pqSwap(p->a, i, par); i = par;
    }
}
static void pqDown(PQ* p, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, b = i;
        if (l < p->n && p->a[l].dist < p->a[b].dist) b = l;
        if (r < p->n && p->a[r].dist < p->a[b].dist) b = r;
        if (b == i) break;
        pqSwap(p->a, i, b); i = b;
    }
}
static void pqPush(PQ* p, Item x) { p->a[p->n] = x; pqUp(p, p->n++); }
static Item pqPop(PQ* p) { Item x = p->a[0]; p->a[0] = p->a[--p->n]; pqDown(p, 0); return x; }

static long long* dijkstra(int n, Adj* g, int src) {
    const long long INF = (1LL << 62);
    long long* dist = (long long*)malloc((size_t)n * sizeof(long long));
    for (int i = 0; i < n; i++) dist[i] = INF;
    dist[src] = 0;
    PQ pq = { .a = (Item*)malloc((size_t)(n * 20 + 5) * sizeof(Item)), .n = 0 };
    pqPush(&pq, (Item){0, src});
    while (pq.n) {
        Item cur = pqPop(&pq);
        if (cur.dist != dist[cur.node]) continue;
        Adj* e = &g[cur.node];
        for (int i = 0; i < e->len; i++) {
            int v = e->to[i];
            long long nd = cur.dist + e->w[i];
            if (nd < dist[v]) { dist[v] = nd; pqPush(&pq, (Item){nd, v}); }
        }
    }
    free(pq.a);
    return dist;
}

long long minimumWeight(int n, int** edges, int edgesSize, int* edgesColSize, int src1, int src2, int dest) {
    (void)edgesColSize;
    Adj* g = (Adj*)calloc((size_t)n, sizeof(Adj));
    Adj* rg = (Adj*)calloc((size_t)n, sizeof(Adj));
    for (int i = 0; i < edgesSize; i++) {
        adjAdd(&g[edges[i][0]], edges[i][1], edges[i][2]);
        adjAdd(&rg[edges[i][1]], edges[i][0], edges[i][2]);
    }
    long long* d1 = dijkstra(n, g, src1);
    long long* d2 = dijkstra(n, g, src2);
    long long* dd = dijkstra(n, rg, dest);
    const long long INF = (1LL << 62);
    long long ans = INF;
    for (int i = 0; i < n; i++) {
        if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue;
        long long cand = d1[i] + d2[i] + dd[i];
        if (cand < ans) ans = cand;
    }
    for (int i = 0; i < n; i++) { free(g[i].to); free(g[i].w); free(rg[i].to); free(rg[i].w); }
    free(g); free(rg); free(d1); free(d2); free(dd);
    return ans >= INF ? -1 : ans;
}
