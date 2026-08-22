// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

#include <stdlib.h>

int maxSubarrayLength(int* nums, int numsSize) {
    int n = numsSize, ans = 0;
    int* st = (int*)malloc(n * sizeof(int));
    int top = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (top == 0 || nums[i] > nums[st[top - 1]]) st[top++] = i;
    }
    for (int i = 0; i < n; i++) {
        while (top > 0 && nums[i] > nums[st[top - 1]]) {
            int j = st[--top];
            if (j - i + 1 > ans) ans = j - i + 1;
        }
    }
    free(st);
    return ans;
}
