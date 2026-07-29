// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

static int dfs(int** grid, int m, int n, int i, int j) {
    if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0) return 0;
    grid[i][j] = 0;
    return 1 + dfs(grid, m, n, i + 1, j) + dfs(grid, m, n, i - 1, j) + dfs(grid, m, n, i, j + 1) + dfs(grid, m, n, i, j - 1);
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int best = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j]) {
                int area = dfs(grid, gridSize, gridColSize[i], i, j);
                if (area > best) best = area;
            }
        }
    }
    return best;
}
