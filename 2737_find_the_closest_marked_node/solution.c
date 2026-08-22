// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int node, dist; } EI2737;

static void push2737(EI2737* h, int* hs, EI2737 x) {
    int i = (*hs)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].dist <= h[i].dist) break;
        EI2737 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static EI2737 pop2737(EI2737* h, int* hs) {
    EI2737 top = h[0];
    h[0] = h[--(*hs)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, sm = i;
        if (l < *hs && h[l].dist < h[sm].dist) sm = l;
        if (r < *hs && h[r].dist < h[sm].dist) sm = r;
        if (sm == i) break;
        EI2737 t = h[i]; h[i] = h[sm]; h[sm] = t;
        i = sm;
    }
    return top;
}

int minimumDistance(int n, int** edges, int edgesSize, int* edgesColSize, int s, int* marked, int markedSize) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gSz = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (gSz[u] + 2 > gCap[u]) {
            gCap[u] = gCap[u] ? gCap[u] * 2 : 4;
            g[u] = (int*)realloc(g[u], (size_t)gCap[u] * sizeof(int));
        }
        g[u][gSz[u]++] = v;
        g[u][gSz[u]++] = w;
    }
    bool* mark = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < markedSize; i++) mark[marked[i]] = true;
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = 1 << 30;
    dist[s] = 0;
    EI2737* heap = (EI2737*)malloc((size_t)(n * 8 + 16) * sizeof(EI2737));
    int hs = 0;
    push2737(heap, &hs, (EI2737){s, 0});
    int ans = -1;
    while (hs > 0) {
        EI2737 cur = pop2737(heap, &hs);
        if (mark[cur.node]) { ans = cur.dist; break; }
        if (cur.dist > dist[cur.node]) continue;
        for (int i = 0; i < gSz[cur.node]; i += 2) {
            int nd = cur.dist + g[cur.node][i + 1];
            int to = g[cur.node][i];
            if (nd < dist[to]) {
                dist[to] = nd;
                push2737(heap, &hs, (EI2737){to, nd});
            }
        }
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gSz); free(gCap); free(mark); free(dist); free(heap);
    return ans;
}
