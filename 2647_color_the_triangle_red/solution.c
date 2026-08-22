// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** colorRed(int n, int* returnSize, int** returnColumnSizes) {
    int cap = n * n + 8;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    int* cols = (int*)malloc((size_t)cap * sizeof(int));
    int sz = 0;
    for (int i = 1; i <= n; i++) {
        ans[sz] = (int*)malloc(2 * sizeof(int));
        ans[sz][0] = i; ans[sz][1] = 1;
        cols[sz++] = 2;
    }
    for (int i = n % 2 + 2; i <= n; i += 2) {
        for (int j = 2; j <= 2 * (n - i) + 2; j++) {
            ans[sz] = (int*)malloc(2 * sizeof(int));
            ans[sz][0] = i; ans[sz][1] = j;
            cols[sz++] = 2;
        }
    }
    *returnSize = sz;
    *returnColumnSizes = cols;
    return ans;
}
