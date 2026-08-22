// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* shortestDistanceAfterQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int** g = (int**)malloc((size_t)n * sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        gcap[i] = 4;
        g[i] = (int*)malloc(4 * sizeof(int));
        if (i + 1 < n) g[i][glen[i]++] = i + 1;
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int u = queries[qi][0], v = queries[qi][1];
        if (glen[u] == gcap[u]) {
            gcap[u] *= 2;
            g[u] = (int*)realloc(g[u], (size_t)gcap[u] * sizeof(int));
        }
        g[u][glen[u]++] = v;
        int* q = (int*)malloc((size_t)n * sizeof(int));
        bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
        int qh = 0, qt = 0;
        q[qt++] = 0; vis[0] = true;
        int d = 0, found = -1;
        while (qh < qt && found < 0) {
            int sz = qt - qh;
            for (int k = 0; k < sz; k++) {
                int cur = q[qh++];
                if (cur == n - 1) { found = d; break; }
                for (int j = 0; j < glen[cur]; j++) {
                    int nxt = g[cur][j];
                    if (!vis[nxt]) { vis[nxt] = true; q[qt++] = nxt; }
                }
            }
            d++;
        }
        ans[qi] = found;
        free(q); free(vis);
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap);
    *returnSize = queriesSize;
    return ans;
}
