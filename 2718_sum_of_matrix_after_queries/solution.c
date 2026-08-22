// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

long long matrixSumQueries(int n, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    bool* rowSet = (bool*)calloc((size_t)n, sizeof(bool));
    bool* colSet = (bool*)calloc((size_t)n, sizeof(bool));
    int rowCnt = 0, colCnt = 0;
    long long ans = 0;
    for (int i = queriesSize - 1; i >= 0; i--) {
        int t = queries[i][0], idx = queries[i][1], v = queries[i][2];
        if (t == 0) {
            if (rowSet[idx]) continue;
            rowSet[idx] = true; rowCnt++;
            ans += (long long)v * (n - colCnt);
        } else {
            if (colSet[idx]) continue;
            colSet[idx] = true; colCnt++;
            ans += (long long)v * (n - rowCnt);
        }
    }
    free(rowSet); free(colSet);
    return ans;
}
