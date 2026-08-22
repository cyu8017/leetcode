// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

#include <stdlib.h>

static int*** f;
static int** gridG;
static int mG, nG, kG;
static const int INF = 1 << 30;

static int imax(int a, int b) { return a > b ? a : b; }

static int dfs(int i, int j, int k) {
    if (i < 0 || j < 0 || k < 0) return -INF;
    if (i == 0 && j == 0) return 0;
    if (f[i][j][k] != -1) return f[i][j][k];
    int res = gridG[i][j];
    int nk = k;
    if (gridG[i][j] != 0) nk--;
    int a = dfs(i - 1, j, nk);
    int b = dfs(i, j - 1, nk);
    res += imax(a, b);
    f[i][j][k] = res;
    return res;
}

int maxPathScore(int** grid, int gridSize, int* gridColSize, int k) {
    mG = gridSize; nG = gridColSize[0]; kG = k; gridG = grid;
    f = (int***)malloc((size_t)mG * sizeof(int**));
    for (int i = 0; i < mG; i++) {
        f[i] = (int**)malloc((size_t)nG * sizeof(int*));
        for (int j = 0; j < nG; j++) {
            f[i][j] = (int*)malloc((size_t)(k + 1) * sizeof(int));
            for (int t = 0; t <= k; t++) f[i][j][t] = -1;
        }
    }
    int ans = dfs(mG - 1, nG - 1, k);
    for (int i = 0; i < mG; i++) {
        for (int j = 0; j < nG; j++) free(f[i][j]);
        free(f[i]);
    }
    free(f);
    return ans < 0 ? -1 : ans;
}
