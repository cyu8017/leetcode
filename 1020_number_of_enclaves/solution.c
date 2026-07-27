// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

static void flood(int** grid, int m, int n, int r, int c) {
    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) return;
    grid[r][c] = 0;
    flood(grid, m, n, r + 1, c);
    flood(grid, m, n, r - 1, c);
    flood(grid, m, n, r, c + 1);
    flood(grid, m, n, r, c - 1);
}

int numEnclaves(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    for (int i = 0; i < m; i++) {
        flood(grid, m, n, i, 0);
        flood(grid, m, n, i, n - 1);
    }
    for (int j = 0; j < n; j++) {
        flood(grid, m, n, 0, j);
        flood(grid, m, n, m - 1, j);
    }
    int ans = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            ans += grid[i][j];
    return ans;
}
