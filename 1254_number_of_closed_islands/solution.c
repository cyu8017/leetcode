// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

#include <stdbool.h>
#include <stdlib.h>

static bool flood(int** grid, int m, int n, int sr, int sc) {
    int* stackR = (int*)malloc((size_t)(m * n) * sizeof(int));
    int* stackC = (int*)malloc((size_t)(m * n) * sizeof(int));
    int top = 0;
    stackR[top] = sr;
    stackC[top] = sc;
    top++;
    grid[sr][sc] = 1;
    bool closed = true;
    while (top > 0) {
        int r = stackR[--top];
        int c = stackC[top];
        if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false;
        static const int dr[4] = {1, -1, 0, 0};
        static const int dc[4] = {0, 0, 1, -1};
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                grid[nr][nc] = 1;
                stackR[top] = nr;
                stackC[top] = nc;
                top++;
            }
        }
    }
    free(stackR);
    free(stackC);
    return closed;
}

int closedIsland(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int ans = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 0 && flood(grid, m, n, r, c)) ans++;
        }
    }
    return ans;
}
