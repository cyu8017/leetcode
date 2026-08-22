// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

#include <stdlib.h>

typedef struct { int u, d; } Node2045;

int secondMinimum(int n, int** edges, int edgesSize, int* edgesColSize, int time, int change) {
    (void)edgesColSize;
    int* deg = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; i++) { deg[edges[i][0]]++; deg[edges[i][1]]++; }
    int** g = (int**)malloc(((size_t)n + 1) * sizeof(int*));
    int* gc = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) g[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        g[a][gc[a]++] = b; g[b][gc[b]++] = a;
    }
    int* dist1 = (int*)malloc(((size_t)n + 1) * sizeof(int));
    int* dist2 = (int*)malloc(((size_t)n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) { dist1[i] = -1; dist2[i] = -1; }
    Node2045* q = (Node2045*)malloc((size_t)(n * 4 + 5) * sizeof(Node2045));
    int qh = 0, qt = 0;
    q[qt++] = (Node2045){1, 0};
    dist1[1] = 0;
    while (qh < qt) {
        Node2045 cur = q[qh++];
        for (int i = 0; i < gc[cur.u]; i++) {
            int v = g[cur.u][i];
            int nd = cur.d + 1;
            if (dist1[v] == -1) { dist1[v] = nd; q[qt++] = (Node2045){v, nd}; }
            else if (dist2[v] == -1 && nd > dist1[v]) { dist2[v] = nd; q[qt++] = (Node2045){v, nd}; }
        }
    }
    int steps = dist2[n], ans = 0;
    for (int i = 0; i < steps; i++) {
        if ((ans / change) % 2 == 1) ans += change - ans % change;
        ans += time;
    }
    for (int i = 1; i <= n; i++) free(g[i]);
    free(g); free(gc); free(deg); free(dist1); free(dist2); free(q);
    return ans;
}
