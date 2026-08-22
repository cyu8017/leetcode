// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

#include <stdlib.h>
#include <string.h>

int networkBecomesIdle(int** edges, int edgesSize, int* edgesColSize, int* patience, int patienceSize) {
    (void)edgesColSize;
    int n = patienceSize;
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) { deg[edges[i][0]]++; deg[edges[i][1]]++; }
    int** g = (int**)malloc((size_t)n * sizeof(int*));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) g[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        g[a][gc[a]++] = b; g[b][gc[b]++] = a;
    }
    int* dist = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = -1;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = 0; dist[0] = 0;
    while (qh < qt) {
        int u = q[qh++];
        for (int i = 0; i < gc[u]; i++) {
            int v = g[u][i];
            if (dist[v] == -1) { dist[v] = dist[u] + 1; q[qt++] = v; }
        }
    }
    int ans = 0;
    for (int i = 1; i < n; i++) {
        int round = dist[i] * 2;
        int lastSend = (round - 1) / patience[i] * patience[i];
        int finish = lastSend + round;
        if (finish > ans) ans = finish;
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gc); free(deg); free(dist); free(q);
    return ans + 1;
}
