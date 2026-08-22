// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

#include <stdlib.h>

int minimumTime(int n, int** relations, int relationsSize, int* relationsColSize, int* time, int timeSize) {
    (void)relationsColSize; (void)timeSize;
    int* indeg = (int*)calloc((size_t)n + 1, sizeof(int));
    int* deg = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 0; i < relationsSize; i++) { deg[relations[i][0]]++; indeg[relations[i][1]]++; }
    int** g = (int**)malloc(((size_t)n + 1) * sizeof(int*));
    int* gc = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) g[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    for (int i = 0; i < relationsSize; i++) g[relations[i][0]][gc[relations[i][0]]++] = relations[i][1];
    int* dist = (int*)malloc(((size_t)n + 1) * sizeof(int));
    int* q = (int*)malloc(((size_t)n + 1) * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 1; i <= n; i++) {
        dist[i] = time[i - 1];
        if (indeg[i] == 0) q[qt++] = i;
    }
    while (qh < qt) {
        int u = q[qh++];
        for (int i = 0; i < gc[u]; i++) {
            int v = g[u][i];
            if (dist[u] + time[v - 1] > dist[v]) dist[v] = dist[u] + time[v - 1];
            if (--indeg[v] == 0) q[qt++] = v;
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) if (dist[i] > ans) ans = dist[i];
    for (int i = 1; i <= n; i++) free(g[i]);
    free(g); free(gc); free(deg); free(indeg); free(dist); free(q);
    return ans;
}
