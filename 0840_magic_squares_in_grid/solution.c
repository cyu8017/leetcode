// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

static bool magic(int** grid, int r, int c) {
    int vals[9];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            vals[i * 3 + j] = grid[r + i][c + j];
    int sorted[9];
    memcpy(sorted, vals, sizeof(vals));
    qsort(sorted, 9, sizeof(int), cmp_int);
    for (int i = 0; i < 9; i++) if (sorted[i] != i + 1) return false;
    return
        grid[r][c]+grid[r][c+1]+grid[r][c+2]==15 &&
        grid[r+1][c]+grid[r+1][c+1]+grid[r+1][c+2]==15 &&
        grid[r+2][c]+grid[r+2][c+1]+grid[r+2][c+2]==15 &&
        grid[r][c]+grid[r+1][c]+grid[r+2][c]==15 &&
        grid[r][c+1]+grid[r+1][c+1]+grid[r+2][c+1]==15 &&
        grid[r][c+2]+grid[r+1][c+2]+grid[r+2][c+2]==15 &&
        grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]==15 &&
        grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]==15;
}

int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize, cols = gridColSize[0];
    if (rows < 3 || cols < 3) return 0;
    int ans = 0;
    for (int i = 0; i < rows - 2; i++)
        for (int j = 0; j < cols - 2; j++)
            if (magic(grid, i, j)) ans++;
    return ans;
}
