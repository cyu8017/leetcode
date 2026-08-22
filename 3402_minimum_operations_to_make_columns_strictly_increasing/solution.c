// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0], ans = 0;
    for (int j = 0; j < n; j++) {
        for (int i = 1; i < m; i++) {
            if (grid[i][j] <= grid[i - 1][j]) {
                int need = grid[i - 1][j] + 1;
                ans += need - grid[i][j];
                grid[i][j] = need;
            }
        }
    }
    return ans;
}
