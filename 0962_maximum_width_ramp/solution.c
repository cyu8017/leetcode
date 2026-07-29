// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

#include <stdlib.h>

int maxWidthRamp(int* nums, int numsSize) {
    int* stack = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < numsSize; i++) {
        if (top == 0 || nums[stack[top - 1]] > nums[i]) stack[top++] = i;
    }
    int ans = 0;
    for (int j = numsSize - 1; j >= 0; j--) {
        while (top > 0 && nums[stack[top - 1]] <= nums[j]) {
            int w = j - stack[--top];
            if (w > ans) ans = w;
        }
    }
    free(stack);
    return ans;
}
