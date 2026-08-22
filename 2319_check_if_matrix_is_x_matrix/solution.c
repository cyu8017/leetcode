// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

#include <stdbool.h>

bool checkXMatrix(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int diag = (i == j) || (i + j == n - 1);
            if (diag) {
                if (grid[i][j] == 0) return false;
            } else if (grid[i][j] != 0) {
                return false;
            }
        }
    }
    return true;
}
