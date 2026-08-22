// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

#include <stdlib.h>

static int imax(int a, int b) { return a > b ? a : b; }

int longestSubarray(int* nums, int numsSize) {
    int n = numsSize;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { left[i] = 1; right[i] = 1; }
    for (int i = 1; i < n; i++) if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
    for (int i = n - 2; i >= 0; i--) if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
    int ans = left[0];
    for (int i = 1; i < n; i++) if (left[i] > ans) ans = left[i];
    for (int i = 0; i < n; i++) {
        int a = i > 0 ? left[i - 1] : 0;
        int b = i + 1 < n ? right[i + 1] : 0;
        if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1])
            ans = imax(ans, imax(a + 1, b + 1));
        else
            ans = imax(ans, a + b + 1);
    }
    free(left); free(right);
    return ans;
}
