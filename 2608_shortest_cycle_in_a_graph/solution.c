// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

#include <stdlib.h>

int findShortestCycle(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* head = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    int* next = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    int ec = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        to[ec] = v; next[ec] = head[u]; head[u] = ec++;
        to[ec] = u; next[ec] = head[v]; head[v] = ec++;
    }
    const int INF = 1000000000;
    int ans = INF;
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    int* q = (int*)malloc((size_t)n * sizeof(int));
    for (int start = 0; start < n; start++) {
        for (int i = 0; i < n; i++) { dist[i] = -1; parent[i] = -1; }
        int qh = 0, qt = 0;
        q[qt++] = start;
        dist[start] = 0;
        while (qh < qt) {
            int u = q[qh++];
            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                if (dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q[qt++] = v;
                } else if (parent[u] != v) {
                    int c = dist[u] + dist[v] + 1;
                    if (c < ans) ans = c;
                }
            }
        }
    }
    free(head); free(to); free(next); free(dist); free(parent); free(q);
    return ans == INF ? -1 : ans;
}
