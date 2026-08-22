// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

static int g_ans, g_m, g_n, g_numSelect;
static int** g_matrix;

static void dfs(int col, int chosen, int mask) {
    if (chosen == g_numSelect) {
        int covered = 0;
        for (int i = 0; i < g_m; i++) {
            int ok = 1;
            for (int j = 0; j < g_n; j++) {
                if (g_matrix[i][j] == 1 && ((mask >> j) & 1) == 0) { ok = 0; break; }
            }
            if (ok) covered++;
        }
        if (covered > g_ans) g_ans = covered;
        return;
    }
    if (col == g_n) return;
    dfs(col + 1, chosen + 1, mask | (1 << col));
    dfs(col + 1, chosen, mask);
}

int maximumRows(int** matrix, int matrixSize, int* matrixColSize, int numSelect) {
    g_matrix = matrix; g_m = matrixSize; g_n = matrixColSize[0]; g_numSelect = numSelect; g_ans = 0;
    dfs(0, 0, 0);
    return g_ans;
}
