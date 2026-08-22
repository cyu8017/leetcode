// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

int** reverseSubmatrix(int** grid, int gridSize, int* gridColSize, int x, int y, int k, int* returnSize, int** returnColumnSizes) {
    for (int i = x; i < x + k / 2; i++) {
        int i2 = x + k - 1 - (i - x);
        for (int j = y; j < y + k; j++) {
            int t = grid[i][j]; grid[i][j] = grid[i2][j]; grid[i2][j] = t;
        }
    }
    *returnSize = gridSize;
    *returnColumnSizes = gridColSize;
    return grid;
}
