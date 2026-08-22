// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

#include <stdlib.h>
#include <string.h>

typedef struct { int to, weight; } Edge3970;
typedef struct { long long distance; int node, run; } State3970;

static void heapPush3970(State3970** h, int* hn, int* hcap, State3970 x) {
    if (*hn == *hcap) { *hcap = *hcap ? *hcap * 2 : 8; *h = realloc(*h, (size_t)(*hcap) * sizeof(State3970)); }
    int i = (*hn)++;
    (*h)[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if ((*h)[p].distance <= (*h)[i].distance) break;
        State3970 t = (*h)[p]; (*h)[p] = (*h)[i]; (*h)[i] = t;
        i = p;
    }
}
static State3970 heapPop3970(State3970* h, int* hn) {
    State3970 res = h[0];
    h[0] = h[--(*hn)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *hn && h[l].distance < h[best].distance) best = l;
        if (r < *hn && h[r].distance < h[best].distance) best = r;
        if (best == i) break;
        State3970 t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

long long shortestPath(int n, int** edges, int edgesSize, int* edgesColSize, char* labels, int k) {
    (void)edgesColSize;
    Edge3970** graph = calloc((size_t)n, sizeof(Edge3970*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u] * 2 : 4; graph[u] = realloc(graph[u], (size_t)cap[u] * sizeof(Edge3970)); }
        graph[u][deg[u]++] = (Edge3970){v, w};
    }
    const long long infinity = (1LL << 62);
    long long** distances = malloc((size_t)n * sizeof(long long*));
    for (int node = 0; node < n; node++) {
        distances[node] = malloc((size_t)(k + 1) * sizeof(long long));
        for (int run = 0; run <= k; run++) distances[node][run] = infinity;
    }
    distances[0][1] = 0;
    State3970* heap = NULL; int hn = 0, hcap = 0;
    heapPush3970(&heap, &hn, &hcap, (State3970){0, 0, 1});
    long long ans = -1;
    while (hn > 0) {
        State3970 current = heapPop3970(heap, &hn);
        if (current.distance != distances[current.node][current.run]) continue;
        if (current.node == n - 1) { ans = current.distance; break; }
        for (int i = 0; i < deg[current.node]; i++) {
            Edge3970 edge = graph[current.node][i];
            int nextRun = 1;
            if (labels[current.node] == labels[edge.to]) nextRun = current.run + 1;
            if (nextRun > k) continue;
            long long nextDistance = current.distance + edge.weight;
            if (nextDistance < distances[edge.to][nextRun]) {
                distances[edge.to][nextRun] = nextDistance;
                heapPush3970(&heap, &hn, &hcap, (State3970){nextDistance, edge.to, nextRun});
            }
        }
    }
    for (int i = 0; i < n; i++) { free(graph[i]); free(distances[i]); }
    free(graph); free(deg); free(cap); free(distances); free(heap);
    return ans;
}
