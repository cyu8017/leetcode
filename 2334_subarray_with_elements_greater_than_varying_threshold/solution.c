// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

#include <stdlib.h>

int validSubarraySize(int* nums, int numsSize, int threshold) {
    int n = numsSize;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && nums[stack[top - 1]] >= nums[i]) top--;
        left[i] = top == 0 ? -1 : stack[top - 1];
        stack[top++] = i;
    }
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && nums[stack[top - 1]] >= nums[i]) top--;
        right[i] = top == 0 ? n : stack[top - 1];
        stack[top++] = i;
    }
    int ans = -1;
    for (int i = 0; i < n; i++) {
        int k = right[i] - left[i] - 1;
        if (nums[i] > threshold / k) { ans = k; break; }
    }
    free(left); free(right); free(stack);
    return ans;
}
