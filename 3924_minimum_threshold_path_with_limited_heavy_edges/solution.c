// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

#include <stdlib.h>
#include <string.h>

typedef struct { int to, weight; } Edge3924;

static int can3924(int n, Edge3924** g, int* deg, int source, int target, int k, int threshold) {
    const int inf = 1000000000;
    int* dist = malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = inf;
    dist[source] = 0;
    int* dq = malloc((size_t)(n * (k + 2) + 8) * sizeof(int));
    int head = 0, tail = 0;
    dq[tail++] = source;
    while (head < tail) {
        int u = dq[head++];
        for (int i = 0; i < deg[u]; i++) {
            int cost = g[u][i].weight > threshold ? 1 : 0;
            int v = g[u][i].to;
            if (dist[u] + cost >= dist[v] || dist[u] + cost > k) continue;
            dist[v] = dist[u] + cost;
            if (cost == 0) {
                /* push front */
                if (head > 0) dq[--head] = v;
                else {
                    /* shift */
                    memmove(dq + 1, dq, (size_t)(tail - head) * sizeof(int));
                    tail++;
                    dq[head] = v;
                }
            } else {
                dq[tail++] = v;
            }
        }
    }
    int ok = dist[target] <= k;
    free(dist); free(dq);
    return ok;
}

int minThreshold(int n, int** edges, int edgesSize, int* edgesColSize, int source, int target, int k) {
    (void)edgesColSize;
    if (source == target) return 0;
    Edge3924** g = calloc((size_t)n, sizeof(Edge3924*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    int maxWeight = 0;
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a] * 2 : 4; g[a] = realloc(g[a], (size_t)cap[a] * sizeof(Edge3924)); }
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b] * 2 : 4; g[b] = realloc(g[b], (size_t)cap[b] * sizeof(Edge3924)); }
        g[a][deg[a]++] = (Edge3924){b, w};
        g[b][deg[b]++] = (Edge3924){a, w};
        if (w > maxWeight) maxWeight = w;
    }
    if (!can3924(n, g, deg, source, target, k, maxWeight)) {
        for (int i = 0; i < n; i++) free(g[i]);
        free(g); free(deg); free(cap);
        return -1;
    }
    int lo = 0, hi = maxWeight;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (can3924(n, g, deg, source, target, k, mid)) hi = mid;
        else lo = mid + 1;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(deg); free(cap);
    return lo;
}
