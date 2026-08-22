// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

#include <stdlib.h>

int* maximumSubarrayXor(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = numsSize;
    int** f = (int**)malloc((size_t)n * sizeof(int*));
    int** best = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        f[i] = (int*)calloc((size_t)n, sizeof(int));
        best[i] = (int*)calloc((size_t)n, sizeof(int));
        f[i][i] = best[i][i] = nums[i];
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            f[i][j] = f[i][j - 1] ^ f[i + 1][j];
        }
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            best[i][j] = f[i][j];
            if (best[i][j - 1] > best[i][j]) best[i][j] = best[i][j - 1];
            if (best[i + 1][j] > best[i][j]) best[i][j] = best[i + 1][j];
        }
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) ans[i] = best[queries[i][0]][queries[i][1]];
    for (int i = 0; i < n; i++) { free(f[i]); free(best[i]); }
    free(f); free(best);
    *returnSize = queriesSize;
    return ans;
}
