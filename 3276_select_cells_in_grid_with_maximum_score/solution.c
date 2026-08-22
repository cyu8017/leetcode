// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

#include <stdlib.h>
#include <string.h>

int maxScore(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    /* collect unique values with row lists - values up to 100 typically */
    int maxV = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < gridColSize[i]; j++)
            if (grid[i][j] > maxV) maxV = grid[i][j];
    int* rowCnt = (int*)calloc((size_t)(maxV + 1), sizeof(int));
    int** rows = (int**)calloc((size_t)(maxV + 1), sizeof(int*));
    for (int i = 0; i < m; i++) {
        char seen[101] = {0}; /* values 1..100 in constraints often */
        /* use hash-less: mark seen for this row via scan of existing */
        int* seenVals = (int*)calloc((size_t)(maxV + 1), sizeof(int));
        for (int j = 0; j < gridColSize[i]; j++) {
            int v = grid[i][j];
            if (seenVals[v]) continue;
            seenVals[v] = 1;
            rows[v] = (int*)realloc(rows[v], (size_t)(rowCnt[v] + 1) * sizeof(int));
            rows[v][rowCnt[v]++] = i;
        }
        free(seenVals);
        (void)seen;
    }
    int* arr = (int*)malloc((size_t)(maxV + 1) * sizeof(int));
    int an = 0;
    for (int v = 1; v <= maxV; v++) if (rowCnt[v]) arr[an++] = v;
    for (int i = 0; i < an; i++)
        for (int j = i + 1; j < an; j++)
            if (arr[j] > arr[i]) { int t = arr[i]; arr[i] = arr[j]; arr[j] = t; }
    int N = 1 << m;
    int* dp = (int*)calloc((size_t)N, sizeof(int));
    for (int ai = 0; ai < an; ai++) {
        int v = arr[ai];
        int* ndp = (int*)malloc((size_t)N * sizeof(int));
        memcpy(ndp, dp, (size_t)N * sizeof(int));
        for (int ri = 0; ri < rowCnt[v]; ri++) {
            int bit = 1 << rows[v][ri];
            for (int mask = 0; mask < N; mask++) {
                if (mask & bit) continue;
                int cand = dp[mask] + v;
                int nmask = mask | bit;
                if (cand > ndp[nmask]) ndp[nmask] = cand;
            }
        }
        free(dp); dp = ndp;
    }
    int ans = 0;
    for (int i = 0; i < N; i++) if (dp[i] > ans) ans = dp[i];
    free(dp); free(arr);
    for (int v = 0; v <= maxV; v++) free(rows[v]);
    free(rows); free(rowCnt);
    return ans;
}
