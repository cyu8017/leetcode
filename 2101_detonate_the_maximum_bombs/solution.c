// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

#include <stdlib.h>
#include <stdbool.h>

int maximumDetonation(int** bombs, int bombsSize, int* bombsColSize) {
    (void)bombsColSize;
    int n = bombsSize;
    int** g = (int**)malloc((size_t)n * sizeof(int*));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    int* caps = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) g[i] = NULL;
    for (int i = 0; i < n; i++) {
        long long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            long long dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
            if (dx * dx + dy * dy <= r1 * r1) {
                if (gc[i] == caps[i]) {
                    caps[i] = caps[i] ? caps[i] * 2 : 4;
                    g[i] = (int*)realloc(g[i], (size_t)caps[i] * sizeof(int));
                }
                g[i][gc[i]++] = j;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
        int* q = (int*)malloc((size_t)n * sizeof(int));
        int qh = 0, qt = 0, cnt = 0;
        q[qt++] = i; vis[i] = true;
        while (qh < qt) {
            int u = q[qh++];
            cnt++;
            for (int j = 0; j < gc[u]; j++) {
                int v = g[u][j];
                if (!vis[v]) { vis[v] = true; q[qt++] = v; }
            }
        }
        if (cnt > ans) ans = cnt;
        free(vis); free(q);
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gc); free(caps);
    return ans;
}
