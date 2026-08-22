// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

#include <stdint.h>

long long gridGame(int** grid, int gridSize, int* gridColSize) {
    (void)gridSize;
    int n = gridColSize[0];
    long long top = 0, bottom = 0, ans = INT64_MAX;
    for (int i = 0; i < n; i++) top += grid[0][i];
    for (int i = 0; i < n; i++) {
        top -= grid[0][i];
        long long cur = top > bottom ? top : bottom;
        if (cur < ans) ans = cur;
        bottom += grid[1][i];
    }
    return ans;
}
