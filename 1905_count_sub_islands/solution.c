// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

static int dfs(int** grid1, int** grid2, int rows, int cols, int r, int c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0) return 1;
    grid2[r][c] = 0;
    int ok = grid1[r][c] == 1;
    if (!dfs(grid1, grid2, rows, cols, r + 1, c)) ok = 0;
    if (!dfs(grid1, grid2, rows, cols, r - 1, c)) ok = 0;
    if (!dfs(grid1, grid2, rows, cols, r, c + 1)) ok = 0;
    if (!dfs(grid1, grid2, rows, cols, r, c - 1)) ok = 0;
    return ok;
}

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize) {
    (void)grid1ColSize; (void)grid2ColSize;
    int rows = grid2Size, cols = grid2Size ? grid2ColSize[0] : 0;
    (void)grid1Size;
    int ans = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid2[r][c] == 1 && dfs(grid1, grid2, rows, cols, r, c)) ans++;
        }
    }
    return ans;
}
