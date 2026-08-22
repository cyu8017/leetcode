// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

#include <stdlib.h>

static int cmpIntAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxKDistinct(int* nums, int numsSize, int k, int* returnSize) {
    int* a = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a[i] = nums[i];
    qsort(a, (size_t)numsSize, sizeof(int), cmpIntAsc);
    int* ans = (int*)malloc((size_t)k * sizeof(int));
    int n = 0;
    for (int i = numsSize - 1; i >= 0 && n < k; i--) {
        if (i + 1 < numsSize && a[i] == a[i + 1]) continue;
        ans[n++] = a[i];
    }
    free(a);
    *returnSize = n;
    return ans;
}
