// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

#include <stdlib.h>

int totalSteps(int* nums, int numsSize) {
    int* val = (int*)malloc((size_t)numsSize * sizeof(int));
    int* steps = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;
    int ans = 0;
    for (int i = numsSize - 1; i >= 0; i--) {
        int st = 0;
        while (top > 0 && nums[i] > val[top - 1]) {
            if (steps[top - 1] > st) st = steps[top - 1];
            top--;
            st++;
        }
        if (st > ans) ans = st;
        val[top] = nums[i];
        steps[top] = st;
        top++;
    }
    free(val);
    free(steps);
    return ans;
}
