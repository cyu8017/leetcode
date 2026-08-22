// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        int value = nums[i] < 0 ? -nums[i] : nums[i];
        int index = value - 1;
        if (nums[index] > 0) {
            nums[index] = -nums[index];
        }
    }

    int* result = (int*)malloc((size_t)numsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > 0) {
            result[count++] = i + 1;
        }
    }
    *returnSize = count;
    return result;
}
