// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

#include <stdlib.h>

static int* gnums2615;
static int cmpOrd2615(const void* a, const void* b) {
    int ia = *(const int*)a, ib = *(const int*)b;
    if (gnums2615[ia] != gnums2615[ib]) return gnums2615[ia] - gnums2615[ib];
    return ia - ib;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* distance(int* nums, int numsSize, int* returnSize) {
    long long* ans = (long long*)calloc((size_t)numsSize, sizeof(long long));
    int* order = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) order[i] = i;
    gnums2615 = nums;
    qsort(order, (size_t)numsSize, sizeof(int), cmpOrd2615);
    int i = 0;
    while (i < numsSize) {
        int j = i;
        while (j < numsSize && nums[order[j]] == nums[order[i]]) j++;
        int m = j - i;
        long long* pref = (long long*)malloc((size_t)(m + 1) * sizeof(long long));
        pref[0] = 0;
        for (int t = 0; t < m; t++) pref[t + 1] = pref[t] + order[i + t];
        for (int t = 0; t < m; t++) {
            int idx = order[i + t];
            long long left = (long long)t * idx - pref[t];
            long long right = pref[m] - pref[t + 1] - (long long)(m - 1 - t) * idx;
            ans[idx] = left + right;
        }
        free(pref);
        i = j;
    }
    free(order);
    *returnSize = numsSize;
    return ans;
}
