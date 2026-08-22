// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* minOperations(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    long long* pref = (long long*)calloc((size_t)(numsSize + 1), sizeof(long long));
    for (int i = 0; i < numsSize; i++) pref[i + 1] = pref[i] + nums[i];
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    for (int qi = 0; qi < queriesSize; qi++) {
        int q = queries[qi];
        int lo = 0, hi = numsSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < q) lo = mid + 1;
            else hi = mid;
        }
        int i = lo;
        long long left = (long long)q * i - pref[i];
        long long right = pref[numsSize] - pref[i] - (long long)q * (numsSize - i);
        ans[qi] = left + right;
    }
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
