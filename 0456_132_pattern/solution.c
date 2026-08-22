// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>

bool find132pattern(int* nums, int numsSize) {
    int* stack = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;
    int third = INT_MIN;
    for (int i = numsSize - 1; i >= 0; i--) {
        if (nums[i] < third) {
            free(stack);
            return true;
        }
        while (top > 0 && nums[i] > stack[top - 1]) {
            third = stack[--top];
        }
        stack[top++] = nums[i];
    }
    free(stack);
    return false;
}
