// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    (void)BSize;
    int n = ASize;
    bool* seenA = (bool*)calloc((size_t)n + 1, sizeof(bool));
    bool* seenB = (bool*)calloc((size_t)n + 1, sizeof(bool));
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int common = 0;
    for (int i = 0; i < n; i++) {
        if (seenB[A[i]]) common++;
        seenA[A[i]] = true;
        if (seenA[B[i]]) common++;
        seenB[B[i]] = true;
        ans[i] = common;
    }
    free(seenA); free(seenB);
    *returnSize = n;
    return ans;
}
