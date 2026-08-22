// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

#include <stdlib.h>
#include <limits.h>

typedef struct { int to, w; } Edge3778;
typedef struct { long long cur; int u, used; } State3778;

static void push3778(State3778* h, int* n, State3778 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].cur <= h[i].cur) break;
        State3778 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static State3778 pop3778(State3778* h, int* n) {
    State3778 r = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, rgt = 2 * i + 2, s = i;
        if (l < *n && h[l].cur < h[s].cur) s = l;
        if (rgt < *n && h[rgt].cur < h[s].cur) s = rgt;
        if (s == i) break;
        State3778 t = h[i]; h[i] = h[s]; h[s] = t;
        i = s;
    }
    return r;
}

long long minCostExcludingMax(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    Edge3778** g = (Edge3778**)calloc((size_t)n, sizeof(Edge3778*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u] * 2 : 4; g[u] = (Edge3778*)realloc(g[u], (size_t)cap[u] * sizeof(Edge3778)); }
        g[u][deg[u]++] = (Edge3778){v, w};
        if (deg[v] == cap[v]) { cap[v] = cap[v] ? cap[v] * 2 : 4; g[v] = (Edge3778*)realloc(g[v], (size_t)cap[v] * sizeof(Edge3778)); }
        g[v][deg[v]++] = (Edge3778){u, w};
    }
    long long inf = LLONG_MAX / 4;
    long long (*dist)[2] = calloc((size_t)n, sizeof(*dist));
    for (int i = 0; i < n; i++) { dist[i][0] = inf; dist[i][1] = inf; }
    dist[0][0] = 0;
    State3778* pq = (State3778*)malloc((size_t)(edgesSize * 4 + 16) * sizeof(State3778));
    int psz = 0;
    push3778(pq, &psz, (State3778){0, 0, 0});
    long long answer = dist[n - 1][1];
    while (psz > 0) {
        State3778 t = pop3778(pq, &psz);
        long long cur = t.cur; int u = t.u, used = t.used;
        if (cur > dist[u][used]) continue;
        if (u == n - 1 && used == 1) { answer = cur; break; }
        for (int j = 0; j < deg[u]; j++) {
            int v = g[u][j].to;
            long long w = g[u][j].w;
            long long nxt = cur + w;
            if (nxt < dist[v][used]) {
                dist[v][used] = nxt;
                push3778(pq, &psz, (State3778){nxt, v, used});
            }
            if (used == 0) {
                nxt = cur;
                if (nxt < dist[v][1]) {
                    dist[v][1] = nxt;
                    push3778(pq, &psz, (State3778){nxt, v, 1});
                }
            }
        }
    }
    if (answer == inf) answer = dist[n - 1][1];
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap); free(dist); free(pq);
    return answer;
}
