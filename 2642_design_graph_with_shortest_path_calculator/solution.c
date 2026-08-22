// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

#include <stdlib.h>

typedef struct { int to, w; } Edge;

typedef struct {
    Edge** g;
    int* deg;
    int* cap;
    int n;
} Graph;

Graph* graphCreate(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    Graph* obj = (Graph*)malloc(sizeof(Graph));
    obj->n = n;
    obj->g = (Edge**)calloc((size_t)n, sizeof(Edge*));
    obj->deg = (int*)calloc((size_t)n, sizeof(int));
    obj->cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (obj->deg[u] == obj->cap[u]) {
            obj->cap[u] = obj->cap[u] ? obj->cap[u] * 2 : 4;
            obj->g[u] = (Edge*)realloc(obj->g[u], (size_t)obj->cap[u] * sizeof(Edge));
        }
        obj->g[u][obj->deg[u]++] = (Edge){v, w};
    }
    return obj;
}

void graphAddEdge(Graph* obj, int* edge, int edgeSize) {
    (void)edgeSize;
    int u = edge[0], v = edge[1], w = edge[2];
    if (obj->deg[u] == obj->cap[u]) {
        obj->cap[u] = obj->cap[u] ? obj->cap[u] * 2 : 4;
        obj->g[u] = (Edge*)realloc(obj->g[u], (size_t)obj->cap[u] * sizeof(Edge));
    }
    obj->g[u][obj->deg[u]++] = (Edge){v, w};
}

typedef struct { int node, dist; } DI;

static void siftUp(DI* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].dist <= h[i].dist) break;
        DI t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static void siftDown(DI* h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < n && h[l].dist < h[best].dist) best = l;
        if (r < n && h[r].dist < h[best].dist) best = r;
        if (best == i) break;
        DI t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
}

int graphShortestPath(Graph* obj, int node1, int node2) {
    int n = obj->n;
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = 1 << 30;
    dist[node1] = 0;
    DI* heap = (DI*)malloc((size_t)(n * n + 16) * sizeof(DI));
    int hs = 0;
    heap[hs++] = (DI){node1, 0};
    while (hs > 0) {
        DI cur = heap[0];
        heap[0] = heap[--hs];
        if (hs) siftDown(heap, hs, 0);
        if (cur.node == node2) { free(dist); free(heap); return cur.dist; }
        if (cur.dist > dist[cur.node]) continue;
        for (int i = 0; i < obj->deg[cur.node]; i++) {
            Edge e = obj->g[cur.node][i];
            int nd = cur.dist + e.w;
            if (nd < dist[e.to]) {
                dist[e.to] = nd;
                heap[hs] = (DI){e.to, nd};
                siftUp(heap, hs);
                hs++;
            }
        }
    }
    free(dist); free(heap);
    return -1;
}

void graphFree(Graph* obj) {
    for (int i = 0; i < obj->n; i++) free(obj->g[i]);
    free(obj->g); free(obj->deg); free(obj->cap); free(obj);
}
