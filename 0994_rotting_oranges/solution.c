// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

#include <stdlib.h>

int orangesRotting(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* qr = (int*)malloc((size_t)(m * n) * sizeof(int));
    int* qc = (int*)malloc((size_t)(m * n) * sizeof(int));
    int head = 0, tail = 0, fresh = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 2) { qr[tail] = i; qc[tail] = j; tail++; }
            else if (grid[i][j] == 1) fresh++;
        }
    int minutes = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (head < tail && fresh) {
        int sz = tail - head;
        for (int s = 0; s < sz; s++) {
            int r = qr[head], c = qc[head]; head++;
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    qr[tail] = nr; qc[tail] = nc; tail++;
                }
            }
        }
        minutes++;
    }
    free(qr); free(qc);
    return fresh == 0 ? minutes : -1;
}
