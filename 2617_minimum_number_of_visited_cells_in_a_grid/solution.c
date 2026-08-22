// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

#include <stdlib.h>

int minimumVisitedCells(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = -1;
    }
    int* qr = (int*)malloc((size_t)m * n * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * sizeof(int));
    int qh = 0, qt = 0;
    qr[qt] = 0; qc[qt] = 0; qt++;
    dist[0][0] = 1;
    while (qh < qt) {
        int r = qr[qh], c = qc[qh]; qh++;
        if (r == m - 1 && c == n - 1) {
            int ans = dist[r][c];
            for (int i = 0; i < m; i++) free(dist[i]);
            free(dist); free(qr); free(qc);
            return ans;
        }
        for (int nc = c + 1; nc <= c + grid[r][c] && nc < n; nc++) {
            if (dist[r][nc] == -1) {
                dist[r][nc] = dist[r][c] + 1;
                qr[qt] = r; qc[qt] = nc; qt++;
            }
        }
        for (int nr = r + 1; nr <= r + grid[r][c] && nr < m; nr++) {
            if (dist[nr][c] == -1) {
                dist[nr][c] = dist[r][c] + 1;
                qr[qt] = nr; qc[qt] = c; qt++;
            }
        }
    }
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist); free(qr); free(qc);
    return -1;
}
