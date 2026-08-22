// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool findSafeWalk(int** grid, int gridSize, int* gridColSize, int health) {
    int m = gridSize, n = gridColSize[0];
    int** vis = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        vis[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) vis[i][j] = -1;
    }
    int qh = health - grid[0][0];
    if (qh <= 0) {
        for (int i = 0; i < m; i++) free(vis[i]);
        free(vis);
        return false;
    }
    int* qr = (int*)malloc((size_t)(m * n * 2) * sizeof(int));
    int* qc = (int*)malloc((size_t)(m * n * 2) * sizeof(int));
    int* qhh = (int*)malloc((size_t)(m * n * 2) * sizeof(int));
    int head = 0, tail = 0;
    qr[tail] = 0; qc[tail] = 0; qhh[tail] = qh; tail++;
    vis[0][0] = qh;
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    bool ok = false;
    while (head < tail) {
        int r = qr[head], c = qc[head], h = qhh[head]; head++;
        if (r == m - 1 && c == n - 1) { ok = true; break; }
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            int nh = h - grid[nr][nc];
            if (nh <= 0) continue;
            if (nh > vis[nr][nc]) {
                vis[nr][nc] = nh;
                qr[tail] = nr; qc[tail] = nc; qhh[tail] = nh; tail++;
            }
        }
    }
    free(qr); free(qc); free(qhh);
    for (int i = 0; i < m; i++) free(vis[i]);
    free(vis);
    return ok;
}
