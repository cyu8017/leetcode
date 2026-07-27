// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

#include <stdlib.h>

int shortestPathBinaryMatrix(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    if (grid[0][0] || grid[n - 1][n - 1]) {
        return -1;
    }
    int* qr = (int*)malloc((size_t)n * n * sizeof(int));
    int* qc = (int*)malloc((size_t)n * n * sizeof(int));
    int* qd = (int*)malloc((size_t)n * n * sizeof(int));
    int head = 0, tail = 0;
    qr[tail] = 0;
    qc[tail] = 0;
    qd[tail] = 1;
    tail++;
    grid[0][0] = 1;
    int dr[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
    while (head < tail) {
        int r = qr[head];
        int c = qc[head];
        int dist = qd[head];
        head++;
        if (r == n - 1 && c == n - 1) {
            free(qr);
            free(qc);
            free(qd);
            return dist;
        }
        for (int k = 0; k < 8; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                grid[nr][nc] = 1;
                qr[tail] = nr;
                qc[tail] = nc;
                qd[tail] = dist + 1;
                tail++;
            }
        }
    }
    free(qr);
    free(qc);
    free(qd);
    return -1;
}
