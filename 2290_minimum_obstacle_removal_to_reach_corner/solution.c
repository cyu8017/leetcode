// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

#include <stdlib.h>

int minimumObstacles(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = 1 << 30;
    }
    dist[0][0] = 0;
    int* qr = (int*)malloc((size_t)m * n * 2 * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * 2 * sizeof(int));
    int head = m * n, tail = m * n;
    qr[tail] = 0; qc[tail] = 0; tail++;
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (head < tail) {
        int r = qr[head], c = qc[head];
        head++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nd = dist[r][c] + grid[nr][nc];
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                if (grid[nr][nc] == 0) {
                    head--;
                    qr[head] = nr; qc[head] = nc;
                } else {
                    qr[tail] = nr; qc[tail] = nc; tail++;
                }
            }
        }
    }
    int ans = dist[m - 1][n - 1];
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist); free(qr); free(qc);
    return ans;
}
