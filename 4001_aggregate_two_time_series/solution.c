// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** aggregateTimeSeries(int** series1, int series1Size, int* series1ColSize,
                          int** series2, int series2Size, int* series2ColSize,
                          int* returnSize, int** returnColumnSizes) {
    (void)series1ColSize;
    (void)series2ColSize;
    int m = series1Size, n = series2Size;
    int cap = m + n;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    int* cols = (int*)malloc((size_t)cap * sizeof(int));
    int i = 0, j = 0, k = 0;

    while (i < m && j < n) {
        int t1 = series1[i][0], v1 = series1[i][1];
        int t2 = series2[j][0], v2 = series2[j][1];
        ans[k] = (int*)malloc(2 * sizeof(int));
        cols[k] = 2;
        if (t1 == t2) {
            ans[k][0] = t1;
            ans[k][1] = v1 + v2;
            i++;
            j++;
        } else if (t1 < t2) {
            ans[k][0] = t1;
            ans[k][1] = v1 + v2;
            i++;
        } else {
            ans[k][0] = t2;
            ans[k][1] = v1 + v2;
            j++;
        }
        k++;
    }
    while (i < m) {
        ans[k] = (int*)malloc(2 * sizeof(int));
        ans[k][0] = series1[i][0];
        ans[k][1] = series1[i][1];
        cols[k] = 2;
        i++;
        k++;
    }
    while (j < n) {
        ans[k] = (int*)malloc(2 * sizeof(int));
        ans[k][0] = series2[j][0];
        ans[k][1] = series2[j][1];
        cols[k] = 2;
        j++;
        k++;
    }
    *returnSize = k;
    *returnColumnSizes = cols;
    return ans;
}
