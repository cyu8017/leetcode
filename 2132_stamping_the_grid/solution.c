// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

#include <stdlib.h>
#include <stdbool.h>

bool possibleToStamp(int** grid, int gridSize, int* gridColSize, int stampHeight, int stampWidth) {
    int m = gridSize, n = gridColSize[0];
    int** pref = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) pref[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j];
    #define SUM(r1,c1,r2,c2) (pref[(r2)+1][(c2)+1] - pref[(r1)][(c2)+1] - pref[(r2)+1][(c1)] + pref[(r1)][(c1)])
    int** diff = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) diff[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i + stampHeight - 1 < m; i++) {
        for (int j = 0; j + stampWidth - 1 < n; j++) {
            if (SUM(i, j, i + stampHeight - 1, j + stampWidth - 1) == 0) {
                diff[i][j]++;
                diff[i][j + stampWidth]--;
                diff[i + stampHeight][j]--;
                diff[i + stampHeight][j + stampWidth]++;
            }
        }
    }
    int** cur = (int**)malloc((size_t)m * sizeof(int*));
    bool ok = true;
    for (int i = 0; i < m; i++) {
        cur[i] = (int*)calloc((size_t)n, sizeof(int));
        for (int j = 0; j < n; j++) {
            int v = diff[i][j];
            if (i > 0) v += cur[i - 1][j];
            if (j > 0) v += cur[i][j - 1];
            if (i > 0 && j > 0) v -= cur[i - 1][j - 1];
            cur[i][j] = v;
            if (grid[i][j] == 0 && v == 0) ok = false;
        }
    }
    for (int i = 0; i <= m; i++) { free(pref[i]); free(diff[i]); }
    free(pref); free(diff);
    for (int i = 0; i < m; i++) free(cur[i]);
    free(cur);
    return ok;
}
