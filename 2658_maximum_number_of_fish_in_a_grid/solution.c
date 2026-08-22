// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

static int dfs2658(int** grid, int m, int n, int r, int c) {
    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0;
    int fish = grid[r][c];
    grid[r][c] = 0;
    return fish + dfs2658(grid, m, n, r + 1, c) + dfs2658(grid, m, n, r - 1, c)
         + dfs2658(grid, m, n, r, c + 1) + dfs2658(grid, m, n, r, c - 1);
}

int findMaxFish(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0], best = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] > 0) {
                int v = dfs2658(grid, m, n, i, j);
                if (v > best) best = v;
            }
    return best;
}
