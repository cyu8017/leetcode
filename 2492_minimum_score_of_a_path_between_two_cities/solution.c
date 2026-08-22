// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int minScore(int n, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize;
    int** to = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int** w = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int* deg = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* cap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        int a = roads[i][0], b = roads[i][1], c = roads[i][2];
        for (int t = 0; t < 2; t++) {
            int u = t ? b : a, v = t ? a : b;
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                to[u] = (int*)realloc(to[u], (size_t)cap[u] * sizeof(int));
                w[u] = (int*)realloc(w[u], (size_t)cap[u] * sizeof(int));
            }
            to[u][deg[u]] = v;
            w[u][deg[u]] = c;
            deg[u]++;
        }
    }
    bool* vis = (bool*)calloc((size_t)(n + 1), sizeof(bool));
    int* q = (int*)malloc((size_t)(n + 5) * sizeof(int));
    int head = 0, tail = 0;
    q[tail++] = 1;
    vis[1] = true;
    int ans = 1 << 30;
    while (head < tail) {
        int u = q[head++];
        for (int i = 0; i < deg[u]; i++) {
            if (w[u][i] < ans) ans = w[u][i];
            int v = to[u][i];
            if (!vis[v]) { vis[v] = true; q[tail++] = v; }
        }
    }
    for (int i = 0; i <= n; i++) { free(to[i]); free(w[i]); }
    free(to); free(w); free(deg); free(cap); free(vis); free(q);
    return ans;
}
