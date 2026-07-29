// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

#include <stdlib.h>

static int n_g;
static int** g;
static int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

static void dfs(int r, int c) {
    if (r < 0 || r >= n_g || c < 0 || c >= n_g || g[r][c] != 1) return;
    g[r][c] = 2;
    for (int d = 0; d < 4; d++) dfs(r + dirs[d][0], c + dirs[d][1]);
}

int shortestBridge(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    n_g = gridSize; g = grid;
    int found = 0;
    for (int i = 0; i < n_g && !found; i++)
        for (int j = 0; j < n_g && !found; j++)
            if (grid[i][j] == 1) { dfs(i, j); found = 1; }
    int* qr = (int*)malloc((size_t)(n_g * n_g) * sizeof(int));
    int* qc = (int*)malloc((size_t)(n_g * n_g) * sizeof(int));
    int* qd = (int*)malloc((size_t)(n_g * n_g) * sizeof(int));
    int head = 0, tail = 0;
    for (int i = 0; i < n_g; i++)
        for (int j = 0; j < n_g; j++)
            if (grid[i][j] == 2) { qr[tail]=i; qc[tail]=j; qd[tail]=0; tail++; }
    while (head < tail) {
        int r = qr[head], c = qc[head], dist = qd[head]; head++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nr >= n_g || nc < 0 || nc >= n_g) continue;
            if (grid[nr][nc] == 1) { free(qr);free(qc);free(qd); return dist; }
            if (grid[nr][nc] == 0) {
                grid[nr][nc] = 2;
                qr[tail]=nr; qc[tail]=nc; qd[tail]=dist+1; tail++;
            }
        }
    }
    free(qr);free(qc);free(qd);
    return -1;
}
