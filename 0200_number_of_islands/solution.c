// LeetCode 0200 - Number of Islands
// https://leetcode.com/problems/number-of-islands/

static void flood(char** grid, int rows, int* cols, int row, int col) {
    if (row < 0 || row >= rows || col < 0 || col >= cols[row] ||
        grid[row][col] != '1') {
        return;
    }
    grid[row][col] = '0';
    flood(grid, rows, cols, row + 1, col);
    flood(grid, rows, cols, row - 1, col);
    flood(grid, rows, cols, row, col + 1);
    flood(grid, rows, cols, row, col - 1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize[0] == 0) {
        return 0;
    }

    int islands = 0;
    for (int row = 0; row < gridSize; ++row) {
        for (int col = 0; col < gridColSize[row]; ++col) {
            if (grid[row][col] == '1') {
                ++islands;
                flood(grid, gridSize, gridColSize, row, col);
            }
        }
    }
    return islands;
}
