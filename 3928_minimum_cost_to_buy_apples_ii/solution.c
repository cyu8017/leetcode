// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

#include <stdlib.h>

typedef struct { int to, empty, full; } Edge3928;
typedef struct { int node; long long dist; } State3928;

static void push3928(State3928** h, int* hn, int* hc, State3928 x) {
    if (*hn == *hc) { *hc = *hc ? *hc * 2 : 8; *h = realloc(*h, (size_t)(*hc) * sizeof(State3928)); }
    int i = (*hn)++;
    (*h)[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if ((*h)[p].dist <= (*h)[i].dist) break;
        State3928 t = (*h)[p]; (*h)[p] = (*h)[i]; (*h)[i] = t; i = p;
    }
}
static State3928 pop3928(State3928* h, int* hn) {
    State3928 res = h[0];
    h[0] = h[--(*hn)];
    int i = 0;
    for (;;) {
        int l = 2*i+1, r = 2*i+2, b = i;
        if (l < *hn && h[l].dist < h[b].dist) b = l;
        if (r < *hn && h[r].dist < h[b].dist) b = r;
        if (b == i) break;
        State3928 t = h[i]; h[i] = h[b]; h[b] = t; i = b;
    }
    return res;
}

static long long* dijkstra3928(int n, Edge3928** g, int* deg, int source, int carrying) {
    const long long inf = 1LL << 62;
    long long* dist = malloc((size_t)n * sizeof(long long));
    for (int i = 0; i < n; i++) dist[i] = inf;
    dist[source] = 0;
    State3928* heap = NULL; int hn = 0, hc = 0;
    push3928(&heap, &hn, &hc, (State3928){source, 0});
    while (hn) {
        State3928 cur = pop3928(heap, &hn);
        if (cur.dist != dist[cur.node]) continue;
        for (int i = 0; i < deg[cur.node]; i++) {
            Edge3928 e = g[cur.node][i];
            int weight = carrying ? e.full : e.empty;
            long long next = cur.dist + weight;
            if (next < dist[e.to]) {
                dist[e.to] = next;
                push3928(&heap, &hn, &hc, (State3928){e.to, next});
            }
        }
    }
    free(heap);
    return dist;
}

long long* minCostToBuyApples(int n, int* prices, int pricesSize, int** roads, int roadsSize, int* roadsColSize, int* returnSize) {
    (void)pricesSize; (void)roadsColSize;
    Edge3928** g = calloc((size_t)n, sizeof(Edge3928*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        int a = roads[i][0], b = roads[i][1], empty = roads[i][2], full = roads[i][2] * roads[i][3];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a]*2 : 4; g[a] = realloc(g[a], (size_t)cap[a]*sizeof(Edge3928)); }
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b]*2 : 4; g[b] = realloc(g[b], (size_t)cap[b]*sizeof(Edge3928)); }
        g[a][deg[a]++] = (Edge3928){b, empty, full};
        g[b][deg[b]++] = (Edge3928){a, empty, full};
    }
    long long* answer = malloc((size_t)n * sizeof(long long));
    const long long inf = 1LL << 62;
    for (int source = 0; source < n; source++) {
        long long* emptyDist = dijkstra3928(n, g, deg, source, 0);
        long long* fullDist = dijkstra3928(n, g, deg, source, 1);
        long long best = prices[source];
        for (int shop = 0; shop < n; shop++) {
            if (emptyDist[shop] == inf || fullDist[shop] == inf) continue;
            long long total = emptyDist[shop] + fullDist[shop] + prices[shop];
            if (total < best) best = total;
        }
        answer[source] = best;
        free(emptyDist); free(fullDist);
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap);
    *returnSize = n;
    return answer;
}
