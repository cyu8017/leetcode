// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

#include <stdlib.h>
#include <string.h>

int** colorBorder(int** grid, int gridSize, int* gridColSize, int row, int col, int color,
                  int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int original = grid[row][col];
    char* seen = (char*)calloc((size_t)m * n, 1);
    int* stackR = (int*)malloc((size_t)m * n * sizeof(int));
    int* stackC = (int*)malloc((size_t)m * n * sizeof(int));
    int* compR = (int*)malloc((size_t)m * n * sizeof(int));
    int* compC = (int*)malloc((size_t)m * n * sizeof(int));
    int top = 0, compSize = 0;
    stackR[top] = row; stackC[top] = col; top++;
    seen[row * n + col] = 1;
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    while (top) {
        top--;
        int r = stackR[top], c = stackC[top];
        compR[compSize] = r; compC[compSize] = c; compSize++;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (grid[nr][nc] != original || seen[nr * n + nc]) continue;
            seen[nr * n + nc] = 1;
            stackR[top] = nr; stackC[top] = nc; top++;
        }
    }
    for (int i = 0; i < compSize; i++) {
        int r = compR[i], c = compC[i];
        int border = 0;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || !seen[nr * n + nc]) {
                border = 1;
                break;
            }
        }
        if (border) grid[r][c] = color;
    }
    *returnSize = m;
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) (*returnColumnSizes)[i] = n;
    free(seen); free(stackR); free(stackC); free(compR); free(compC);
    return grid;
}
