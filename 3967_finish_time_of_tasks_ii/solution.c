// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

#include <stdlib.h>

typedef struct { int to, reverse; } Edge3967;

static long long combine3967(long long minimum, long long maximum, int count, int base) {
    if (count == 0) return base;
    return 2 * maximum - minimum + base;
}

long long minFinishTime(int n, int** edges, int edgesSize, int* edgesColSize, int* baseTime, int baseTimeSize) {
    (void)edgesColSize; (void)baseTimeSize;
    Edge3967** graph = calloc((size_t)n, sizeof(Edge3967*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        int iu = deg[u], iv = deg[v];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u]*2 : 4; graph[u] = realloc(graph[u], (size_t)cap[u]*sizeof(Edge3967)); }
        if (deg[v] == cap[v]) { cap[v] = cap[v] ? cap[v]*2 : 4; graph[v] = realloc(graph[v], (size_t)cap[v]*sizeof(Edge3967)); }
        graph[u][deg[u]++] = (Edge3967){v, iv};
        graph[v][deg[v]++] = (Edge3967){u, iu};
        /* fix reverse after possible realloc - re-set */
        graph[u][deg[u]-1].reverse = deg[v]-1;
        graph[v][deg[v]-1].reverse = deg[u]-1;
    }
    int* parent = malloc((size_t)n * sizeof(int));
    int* parentEdge = malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = -2;
    parent[0] = -1;
    int* order = malloc((size_t)n * sizeof(int));
    int on = 0;
    order[on++] = 0;
    for (int i = 0; i < on; i++) {
        int u = order[i];
        for (int edgeIndex = 0; edgeIndex < deg[u]; edgeIndex++) {
            int to = graph[u][edgeIndex].to;
            if (parent[to] == -2) {
                parent[to] = u;
                parentEdge[to] = graph[u][edgeIndex].reverse;
                order[on++] = to;
            }
        }
    }
    long long** incoming = malloc((size_t)n * sizeof(long long*));
    for (int i = 0; i < n; i++) incoming[i] = calloc((size_t)(deg[i] > 0 ? deg[i] : 1), sizeof(long long));
    for (int oi = n - 1; oi > 0; oi--) {
        int u = order[oi];
        long long minimum = 1LL << 62, maximum = -1;
        int count = 0;
        for (int edgeIndex = 0; edgeIndex < deg[u]; edgeIndex++) {
            if (edgeIndex == parentEdge[u]) continue;
            long long value = incoming[u][edgeIndex];
            if (value < minimum) minimum = value;
            if (value > maximum) maximum = value;
            count++;
        }
        long long value = combine3967(minimum, maximum, count, baseTime[u]);
        int parentNode = parent[u];
        int reverseIndex = graph[u][parentEdge[u]].reverse;
        incoming[parentNode][reverseIndex] = value;
    }
    long long answer = 1LL << 62;
    for (int oi = 0; oi < on; oi++) {
        int u = order[oi];
        long long min1 = 1LL << 62, min2 = 1LL << 62;
        long long max1 = -1, max2 = -1;
        int minIndex = -1, maxIndex = -1;
        for (int i = 0; i < deg[u]; i++) {
            long long value = incoming[u][i];
            if (value < min1) { min2 = min1; min1 = value; minIndex = i; }
            else if (value < min2) min2 = value;
            if (value > max1) { max2 = max1; max1 = value; maxIndex = i; }
            else if (value > max2) max2 = value;
        }
        long long rootValue = combine3967(min1, max1, deg[u], baseTime[u]);
        if (rootValue < answer) answer = rootValue;
        for (int i = 0; i < deg[u]; i++) {
            Edge3967 edge = graph[u][i];
            if (edge.to == parent[u]) continue;
            if (deg[u] == 1) {
                incoming[edge.to][edge.reverse] = baseTime[u];
                continue;
            }
            long long minimum = min1, maximum = max1;
            if (i == minIndex) minimum = min2;
            if (i == maxIndex) maximum = max2;
            incoming[edge.to][edge.reverse] = combine3967(minimum, maximum, deg[u] - 1, baseTime[u]);
        }
    }
    for (int i = 0; i < n; i++) { free(graph[i]); free(incoming[i]); }
    free(graph); free(deg); free(cap); free(parent); free(parentEdge); free(order); free(incoming);
    return answer;
}
