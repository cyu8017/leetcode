// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

#include <stdlib.h>

#define INF3555 (1 << 30)

static int f3555(int* nums, int i, int j) {
    int mi = INF3555, mx = -INF3555;
    int l = -1, r = -1;
    for (int p = i; p <= j; p++) {
        if (nums[p] < mx) r = p;
        else mx = nums[p];
        int q = j - p + i;
        if (nums[q] > mi) l = q;
        else mi = nums[q];
    }
    if (r == -1) return 0;
    return r - l + 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minSubarraySort(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int sz = n - k + 1;
    int* ans = (int*)malloc((size_t)sz * sizeof(int));
    for (int i = 0; i <= n - k; i++) ans[i] = f3555(nums, i, i + k - 1);
    *returnSize = sz;
    return ans;
}
