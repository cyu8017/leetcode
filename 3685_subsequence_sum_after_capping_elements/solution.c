// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* subsequenceSumAfterCapping(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int* sorted = (int*)malloc((size_t)n * sizeof(int));
    memcpy(sorted, nums, (size_t)n * sizeof(int));
    qsort(sorted, (size_t)n, sizeof(int), cmpInt);
    bool* ans = (bool*)calloc((size_t)n, sizeof(bool));
    bool* reach = (bool*)calloc((size_t)(k + 1), sizeof(bool));
    reach[0] = true;
    int idx = 0;
    bool* tmp = (bool*)malloc((size_t)(k + 1) * sizeof(bool));
    for (int x = 1; x <= n; x++) {
        while (idx < n && sorted[idx] <= x) {
            int v = sorted[idx];
            for (int s = k; s >= v; s--) {
                if (reach[s - v]) reach[s] = true;
            }
            idx++;
        }
        memcpy(tmp, reach, (size_t)(k + 1) * sizeof(bool));
        int rem = n - idx;
        for (int s = 0; s <= k; s++) {
            if (!reach[s]) continue;
            for (int t = 1; t <= rem && s + t * x <= k; t++) {
                tmp[s + t * x] = true;
            }
        }
        ans[x - 1] = tmp[k];
    }
    free(sorted); free(reach); free(tmp);
    *returnSize = n;
    return ans;
}
