// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

#include <stdlib.h>

static int ans2174;

static void dfs2174(int** grid, int m, int n, int* onesR, int* onesC, int onesN, int idx, int flips) {
    if (flips >= ans2174) return;
    while (idx < onesN && grid[onesR[idx]][onesC[idx]] == 0) idx++;
    if (idx == onesN) { ans2174 = flips; return; }
    int r = onesR[idx], c = onesC[idx];
    int* chR = (int*)malloc((size_t)n * sizeof(int));
    int* chC = (int*)malloc((size_t)n * sizeof(int));
    int cn = 0;
    for (int j = 0; j < n; j++) if (grid[r][j] == 1) {
        grid[r][j] = 0; chR[cn] = r; chC[cn] = j; cn++;
    }
    dfs2174(grid, m, n, onesR, onesC, onesN, idx + 1, flips + 1);
    for (int i = 0; i < cn; i++) grid[chR[i]][chC[i]] = 1;
    cn = 0;
    int* chR2 = (int*)malloc((size_t)m * sizeof(int));
    int* chC2 = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) if (grid[i][c] == 1) {
        grid[i][c] = 0; chR2[cn] = i; chC2[cn] = c; cn++;
    }
    dfs2174(grid, m, n, onesR, onesC, onesN, idx + 1, flips + 1);
    for (int i = 0; i < cn; i++) grid[chR2[i]][chC2[i]] = 1;
    free(chR); free(chC); free(chR2); free(chC2);
}

int removeOnes(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* onesR = (int*)malloc((size_t)m * n * sizeof(int));
    int* onesC = (int*)malloc((size_t)m * n * sizeof(int));
    int onesN = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 1) { onesR[onesN] = i; onesC[onesN] = j; onesN++; }
    if (onesN == 0) { free(onesR); free(onesC); return 0; }
    ans2174 = m + n;
    dfs2174(grid, m, n, onesR, onesC, onesN, 0, 0);
    free(onesR); free(onesC);
    return ans2174;
}
