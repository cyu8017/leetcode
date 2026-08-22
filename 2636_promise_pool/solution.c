// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

#include <stdlib.h>

typedef int (*JobFn)(void);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* promisePool(JobFn* functions, int functionsSize, int n, int* returnSize) {
    (void)n;
    int* ans = (int*)malloc((size_t)functionsSize * sizeof(int));
    for (int i = 0; i < functionsSize; i++) ans[i] = functions[i]();
    *returnSize = functionsSize;
    return ans;
}
