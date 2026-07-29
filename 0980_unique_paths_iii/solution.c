// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

static int m_g, n_g, ans_g;
static int** g;

static void dfs(int r, int c, int remain) {
    if (g[r][c] == 2) { if (remain == 1) ans_g++; return; }
    int temp = g[r][c];
    g[r][c] = -1;
    static int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    for (int d = 0; d < 4; d++) {
        int nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr >= 0 && nr < m_g && nc >= 0 && nc < n_g && g[nr][nc] != -1)
            dfs(nr, nc, remain - 1);
    }
    g[r][c] = temp;
}

int uniquePathsIII(int** grid, int gridSize, int* gridColSize) {
    m_g = gridSize; n_g = gridColSize[0]; g = grid;
    int empty = 0, sr = 0, sc = 0;
    for (int i = 0; i < m_g; i++)
        for (int j = 0; j < n_g; j++) {
            if (grid[i][j] != -1) empty++;
            if (grid[i][j] == 1) { sr = i; sc = j; }
        }
    ans_g = 0;
    dfs(sr, sc, empty);
    return ans_g;
}
