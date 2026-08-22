// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

#include <stdlib.h>

int* maximumLength(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* left = (int*)malloc(n * sizeof(int));
    int* right = (int*)malloc(n * sizeof(int));
    int* st = (int*)malloc(n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && nums[st[top - 1]] < nums[i]) top--;
        left[i] = top == 0 ? -1 : st[top - 1];
        st[top++] = i;
    }
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && nums[st[top - 1]] <= nums[i]) top--;
        right[i] = top == 0 ? n : st[top - 1];
        st[top++] = i;
    }
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
    free(left); free(right); free(st);
    *returnSize = n;
    return ans;
}
