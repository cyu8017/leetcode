// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

#include <stdlib.h>
#include <string.h>

typedef struct { int node, hops, dist; } ST2714;

static void push2714(ST2714* h, int* hs, ST2714 x) {
    int i = (*hs)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].dist <= h[i].dist) break;
        ST2714 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static ST2714 pop2714(ST2714* h, int* hs) {
    ST2714 top = h[0];
    h[0] = h[--(*hs)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, sm = i;
        if (l < *hs && h[l].dist < h[sm].dist) sm = l;
        if (r < *hs && h[r].dist < h[sm].dist) sm = r;
        if (sm == i) break;
        ST2714 t = h[i]; h[i] = h[sm]; h[sm] = t;
        i = sm;
    }
    return top;
}

int shortestPathWithHops(int n, int** edges, int edgesSize, int* edgesColSize, int s, int d, int k) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gSz = (int*)calloc((size_t)n, sizeof(int));
    int* gCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        for (int t = 0; t < 2; t++) {
            int a = t ? v : u, b = t ? u : v;
            if (gSz[a] + 2 > gCap[a]) {
                gCap[a] = gCap[a] ? gCap[a] * 2 : 8;
                g[a] = (int*)realloc(g[a], (size_t)gCap[a] * sizeof(int));
            }
            g[a][gSz[a]++] = b;
            g[a][gSz[a]++] = w;
        }
    }
    int** dist = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dist[i] = (int*)malloc((size_t)(k + 1) * sizeof(int));
        for (int j = 0; j <= k; j++) dist[i][j] = 1 << 30;
    }
    dist[s][0] = 0;
    ST2714* heap = (ST2714*)malloc((size_t)(n * (k + 1) * 8 + 16) * sizeof(ST2714));
    int hs = 0;
    push2714(heap, &hs, (ST2714){s, 0, 0});
    int ans = -1;
    while (hs > 0) {
        ST2714 cur = pop2714(heap, &hs);
        if (cur.node == d) { ans = cur.dist; break; }
        if (cur.dist > dist[cur.node][cur.hops]) continue;
        for (int i = 0; i < gSz[cur.node]; i += 2) {
            int to = g[cur.node][i], w = g[cur.node][i + 1];
            int nd = cur.dist + w;
            if (nd < dist[to][cur.hops]) {
                dist[to][cur.hops] = nd;
                push2714(heap, &hs, (ST2714){to, cur.hops, nd});
            }
            if (cur.hops < k && cur.dist < dist[to][cur.hops + 1]) {
                dist[to][cur.hops + 1] = cur.dist;
                push2714(heap, &hs, (ST2714){to, cur.hops + 1, cur.dist});
            }
        }
    }
    for (int i = 0; i < n; i++) { free(g[i]); free(dist[i]); }
    free(g); free(gSz); free(gCap); free(dist); free(heap);
    return ans;
}
