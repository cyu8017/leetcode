// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

#include <stdlib.h>

int minimumSum(int* nums, int numsSize) {
    int n = numsSize;
    int* left = (int*)malloc(n * sizeof(int));
    int* right = (int*)malloc(n * sizeof(int));
    int mn = 1 << 30;
    for (int i = 0; i < n; i++) { left[i] = mn; if (nums[i] < mn) mn = nums[i]; }
    mn = 1 << 30;
    for (int i = n - 1; i >= 0; i--) { right[i] = mn; if (nums[i] < mn) mn = nums[i]; }
    int ans = 1 << 30;
    for (int j = 1; j < n - 1; j++) {
        if (left[j] < nums[j] && right[j] < nums[j]) {
            int cand = left[j] + nums[j] + right[j];
            if (cand < ans) ans = cand;
        }
    }
    free(left); free(right);
    return ans == (1 << 30) ? -1 : ans;
}
