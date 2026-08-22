// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

#include <stdlib.h>

int longestAlternating(int* nums, int numsSize) {
    int n = numsSize;
    int* l1 = (int*)malloc((size_t)n * sizeof(int));
    int* l2 = (int*)malloc((size_t)n * sizeof(int));
    int* r1 = (int*)malloc((size_t)n * sizeof(int));
    int* r2 = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { l1[i]=l2[i]=r1[i]=r2[i]=1; }
    int ans = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i-1] < nums[i]) l1[i] = l2[i-1] + 1;
        else if (nums[i-1] > nums[i]) l2[i] = l1[i-1] + 1;
        if (l1[i] > ans) ans = l1[i];
        if (l2[i] > ans) ans = l2[i];
    }
    for (int i = n - 2; i >= 0; i--) {
        if (nums[i+1] > nums[i]) r1[i] = r2[i+1] + 1;
        else if (nums[i+1] < nums[i]) r2[i] = r1[i+1] + 1;
    }
    for (int i = 1; i < n - 1; i++) {
        if (nums[i-1] < nums[i+1]) {
            int v = l2[i-1] + r2[i+1];
            if (v > ans) ans = v;
        } else if (nums[i-1] > nums[i+1]) {
            int v = l1[i-1] + r1[i+1];
            if (v > ans) ans = v;
        }
    }
    free(l1); free(l2); free(r1); free(r2);
    return ans;
}
