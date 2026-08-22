// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

#include <stdlib.h>

typedef struct { int dis, u; } Pair;
typedef struct { int v, w; } Edge;
typedef struct { Pair* a; int n, cap; } MinHeap;
static void hpush(MinHeap* h, Pair p) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap*2 : 16; h->a = (Pair*)realloc(h->a, (size_t)h->cap*sizeof(Pair)); }
    int i = h->n++; h->a[i] = p;
    while (i > 0) { int par=(i-1)/2; if (h->a[par].dis <= h->a[i].dis) break; Pair t=h->a[par]; h->a[par]=h->a[i]; h->a[i]=t; i=par; }
}
static Pair hpop(MinHeap* h) {
    Pair r = h->a[0]; h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l=2*i+1,rg=2*i+2,m=i;
        if (l<h->n && h->a[l].dis < h->a[m].dis) m=l;
        if (rg<h->n && h->a[rg].dis < h->a[m].dis) m=rg;
        if (m==i) break;
        Pair t=h->a[i]; h->a[i]=h->a[m]; h->a[m]=t; i=m;
    }
    return r;
}

int* minimumTime(int n, int** edges, int edgesSize, int* edgesColSize, int* disappear, int disappearSize, int* returnSize) {
    (void)edgesColSize; (void)disappearSize;
    Edge** g = (Edge**)calloc((size_t)n, sizeof(Edge*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (gsz[u]==gcap[u]) { gcap[u]=gcap[u]?gcap[u]*2:2; g[u]=(Edge*)realloc(g[u],(size_t)gcap[u]*sizeof(Edge)); }
        if (gsz[v]==gcap[v]) { gcap[v]=gcap[v]?gcap[v]*2:2; g[v]=(Edge*)realloc(g[v],(size_t)gcap[v]*sizeof(Edge)); }
        g[u][gsz[u]++] = (Edge){v, w};
        g[v][gsz[v]++] = (Edge){u, w};
    }
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = 1 << 30;
    dist[0] = 0;
    MinHeap pq = {NULL, 0, 0};
    hpush(&pq, (Pair){0, 0});
    while (pq.n > 0) {
        Pair cur = hpop(&pq);
        int du = cur.dis, u = cur.u;
        if (du > dist[u]) continue;
        for (int i = 0; i < gsz[u]; i++) {
            int v = g[u][i].v, w = g[u][i].w;
            if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                dist[v] = dist[u] + w;
                hpush(&pq, (Pair){dist[v], v});
            }
        }
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = dist[i] < disappear[i] ? dist[i] : -1;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap); free(dist); free(pq.a);
    *returnSize = n;
    return ans;
}
