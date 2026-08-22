// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingAndRepeatedValues(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    (void)gridColSize;
    int n = gridSize;
    int* freq = (int*)calloc((size_t)(n * n + 1), sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            freq[grid[i][j]]++;
        }
    }
    int rep = 0, miss = 0;
    for (int i = 1; i <= n * n; i++) {
        if (freq[i] == 2) rep = i;
        if (freq[i] == 0) miss = i;
    }
    free(freq);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = rep;
    ans[1] = miss;
    *returnSize = 2;
    return ans;
}
