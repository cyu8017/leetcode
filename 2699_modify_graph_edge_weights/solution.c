// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

#include <stdlib.h>
#include <string.h>

typedef struct { int node, dist; } GI2699;

static void push2699(GI2699* h, int* hs, GI2699 x) {
    int i = (*hs)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].dist <= h[i].dist) break;
        GI2699 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static GI2699 pop2699(GI2699* h, int* hs) {
    GI2699 top = h[0];
    h[0] = h[--(*hs)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, sm = i;
        if (l < *hs && h[l].dist < h[sm].dist) sm = l;
        if (r < *hs && h[r].dist < h[sm].dist) sm = r;
        if (sm == i) break;
        GI2699 t = h[i]; h[i] = h[sm]; h[sm] = t;
        i = sm;
    }
    return top;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** modifiedGraphEdges(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination, int target, int* returnSize, int** returnColumnSizes) {
    (void)edgesColSize;
    const int INF = 2000000000;
    int** g = (int**)calloc((size_t)n, sizeof(int*)); /* pairs to,idx */
    int* gSz = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int t = 0; t < 2; t++) {
            int a = t ? v : u, b = t ? u : v;
            if (gSz[a] + 2 > gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 8;
                g[a] = (int*)realloc(g[a], (size_t)gCap[a] * sizeof(int));
            }
            g[a][gSz[a]++] = b;
            g[a][gSz[a]++] = i;
        }
    }
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    GI2699* heap = (GI2699*)malloc((size_t)(n * edgesSize + 16) * sizeof(GI2699));

    #define DIJKSTRA(ignoreNeg) do { \
        for (int __i = 0; __i < n; __i++) dist[__i] = INF; \
        dist[source] = 0; \
        int hs = 0; \
        push2699(heap, &hs, (GI2699){source, 0}); \
        while (hs > 0) { \
            GI2699 cur = pop2699(heap, &hs); \
            if (cur.dist != dist[cur.node]) continue; \
            for (int __j = 0; __j < gSz[cur.node]; __j += 2) { \
                int to = g[cur.node][__j], idx = g[cur.node][__j + 1]; \
                int w = edges[idx][2]; \
                if (w == -1) { if (ignoreNeg) continue; w = 1; } \
                if (cur.dist + w < dist[to]) { \
                    dist[to] = cur.dist + w; \
                    push2699(heap, &hs, (GI2699){to, dist[to]}); \
                } \
            } \
        } \
    } while (0)

    DIJKSTRA(1);
    if (dist[destination] < target) {
        for (int i = 0; i < n; i++) free(g[i]);
        free(g); free(gSz); free(gCap); free(dist); free(heap);
        *returnSize = 0; *returnColumnSizes = NULL; return NULL;
    }
    int matched = dist[destination] == target;
    for (int i = 0; i < edgesSize; i++) {
        if (edges[i][2] != -1) continue;
        if (matched) { edges[i][2] = INF; continue; }
        edges[i][2] = 1;
        DIJKSTRA(0);
        if (dist[destination] <= target) {
            edges[i][2] += target - dist[destination];
            matched = 1;
        }
    }
    DIJKSTRA(0);
    if (dist[destination] != target) {
        for (int i = 0; i < n; i++) free(g[i]);
        free(g); free(gSz); free(gCap); free(dist); free(heap);
        *returnSize = 0; *returnColumnSizes = NULL; return NULL;
    }
    int** ans = (int**)malloc((size_t)edgesSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)edgesSize * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        ans[i] = (int*)malloc(3 * sizeof(int));
        ans[i][0] = edges[i][0]; ans[i][1] = edges[i][1]; ans[i][2] = edges[i][2];
        (*returnColumnSizes)[i] = 3;
    }
    *returnSize = edgesSize;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gSz); free(gCap); free(dist); free(heap);
    return ans;
#undef DIJKSTRA
}
