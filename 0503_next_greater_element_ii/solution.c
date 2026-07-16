// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

#include <stdlib.h>

int* nextGreaterElements(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc((size_t)numsSize * sizeof(int));
    int stack[50000];
    int top = 0;

    for (int index = 0; index < numsSize; index++) {
        result[index] = -1;
    }

    for (int index = 0; index < numsSize * 2; index++) {
        const int value = nums[index % numsSize];
        while (top > 0 && nums[stack[top - 1]] < value) {
            result[stack[--top]] = value;
        }
        if (index < numsSize) {
            stack[top++] = index;
        }
    }

    *returnSize = numsSize;
    return result;
}
