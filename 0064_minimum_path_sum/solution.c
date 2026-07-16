// LeetCode 0064 - Minimum Path Sum
// https://leetcode.com/problems/minimum-path-sum/

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i == 0 && j == 0) {
                continue;
            }
            if (i == 0) {
                grid[i][j] += grid[i][j - 1];
            } else if (j == 0) {
                grid[i][j] += grid[i - 1][j];
            } else {
                int up = grid[i - 1][j];
                int left = grid[i][j - 1];
                grid[i][j] += up < left ? up : left;
            }
        }
    }

    return grid[rows - 1][cols - 1];
}
