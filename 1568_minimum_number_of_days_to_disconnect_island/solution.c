// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

#include <stdlib.h>

static int islands1568(int** grid, int m, int n) {
    char** seen = (char**)malloc((size_t)m * sizeof(char*));
    for (int i = 0; i < m; i++) seen[i] = (char*)calloc((size_t)n, 1);
    int count = 0;
    int* stack = (int*)malloc((size_t)m * n * 2 * sizeof(int));
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] && !seen[r][c]) {
                count++;
                int top = 0;
                stack[top++] = r; stack[top++] = c;
                seen[r][c] = 1;
                while (top) {
                    int y = stack[--top];
                    int x = stack[--top];
                    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
                    for (int d = 0; d < 4; d++) {
                        int nx = x + dirs[d][0], ny = y + dirs[d][1];
                        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] && !seen[nx][ny]) {
                            seen[nx][ny] = 1;
                            stack[top++] = nx; stack[top++] = ny;
                        }
                    }
                }
            }
        }
    }
    for (int i = 0; i < m; i++) free(seen[i]);
    free(seen); free(stack);
    return count;
}

int minDays(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    if (islands1568(grid, m, n) != 1) return 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c]) {
                grid[r][c] = 0;
                if (islands1568(grid, m, n) != 1) {
                    grid[r][c] = 1;
                    return 1;
                }
                grid[r][c] = 1;
            }
        }
    }
    return 2;
}
