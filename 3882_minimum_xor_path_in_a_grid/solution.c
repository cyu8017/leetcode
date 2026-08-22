// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minXor(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize, cols = gridColSize[0];
    bool (*dp)[1024] = calloc((size_t)cols, sizeof(*dp));
    for (int row = 0; row < rows; row++) {
        bool left[1024];
        memset(left, 0, sizeof(left));
        for (int col = 0; col < cols; col++) {
            bool next[1024];
            memset(next, 0, sizeof(next));
            int value = grid[row][col];
            if (row == 0 && col == 0) next[value] = true;
            else {
                for (int xorv = 0; xorv < 1024; xorv++) {
                    if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true;
                }
            }
            memcpy(dp[col], next, sizeof(next));
            memcpy(left, next, sizeof(next));
        }
    }
    int ans = -1;
    for (int xorv = 0; xorv < 1024; xorv++) {
        if (dp[cols - 1][xorv]) { ans = xorv; break; }
    }
    free(dp);
    return ans;
}
