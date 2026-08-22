// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

static int m_g, n_g, **grid_g, dirs[5] = {-1,0,1,0,-1};
static int dfs(int i, int j) {
    int s = grid_g[i][j]; grid_g[i][j] = 0;
    for (int d = 0; d < 4; d++) {
        int x = i + dirs[d], y = j + dirs[d + 1];
        if (x >= 0 && x < m_g && y >= 0 && y < n_g && grid_g[x][y] > 0) s += dfs(x, y);
    }
    return s;
}
int countIslands(int** grid, int gridSize, int* gridColSize, int k) {
    m_g = gridSize; n_g = gridColSize[0]; grid_g = grid;
    int ans = 0;
    for (int i = 0; i < m_g; i++)
        for (int j = 0; j < n_g; j++)
            if (grid[i][j] > 0 && dfs(i, j) % k == 0) ans++;
    return ans;
}
