// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

#include <stdlib.h>

static int transform(int value, int a, int b, int c) {
    return a * value * value + b * value + c;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortTransformedArray(int* nums, int numsSize, int a, int b, int c, int* returnSize) {
    int left = 0;
    int right = numsSize - 1;
    int* result = (int*)malloc((size_t)numsSize * sizeof(int));
    int index = a > 0 ? numsSize - 1 : 0;
    int step = a > 0 ? -1 : 1;

    while (left <= right) {
        int leftValue = transform(nums[left], a, b, c);
        int rightValue = transform(nums[right], a, b, c);

        if (a > 0) {
            if (leftValue > rightValue) {
                result[index] = leftValue;
                left += 1;
            } else {
                result[index] = rightValue;
                right -= 1;
            }
        } else if (leftValue < rightValue) {
            result[index] = leftValue;
            left += 1;
        } else {
            result[index] = rightValue;
            right -= 1;
        }

        index += step;
    }

    *returnSize = numsSize;
    return result;
}
