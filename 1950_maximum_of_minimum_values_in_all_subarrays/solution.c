// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

#include <stdlib.h>

int* findMaximums(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top && nums[stack[top - 1]] >= nums[i]) top--;
        left[i] = top ? stack[top - 1] : -1;
        stack[top++] = i;
    }
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top && nums[stack[top - 1]] >= nums[i]) top--;
        right[i] = top ? stack[top - 1] : n;
        stack[top++] = i;
    }
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        int length = right[i] - left[i] - 1;
        if (nums[i] > ans[length - 1]) ans[length - 1] = nums[i];
    }
    for (int i = n - 2; i >= 0; i--) {
        if (ans[i + 1] > ans[i]) ans[i] = ans[i + 1];
    }
    free(left); free(right); free(stack);
    *returnSize = n;
    return ans;
}
