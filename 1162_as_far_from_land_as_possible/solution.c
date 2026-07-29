// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

#include <stdlib.h>

int maxDistance(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int* qr = (int*)malloc((size_t)n * n * sizeof(int));
    int* qc = (int*)malloc((size_t)n * n * sizeof(int));
    int qs = 0, qe = 0;
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == 1) { qr[qe] = r; qc[qe] = c; qe++; }
    if (qe == 0 || qe == n * n) { free(qr); free(qc); return -1; }
    int dist = -1;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (qs < qe) {
        dist++;
        int sz = qe - qs;
        for (int i = 0; i < sz; i++) {
            int r = qr[qs], c = qc[qs]; qs++;
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    qr[qe] = nr; qc[qe] = nc; qe++;
                }
            }
        }
    }
    free(qr); free(qc);
    return dist;
}
