// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc((size_t)numsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        int value = nums[i] < 0 ? -nums[i] : nums[i];
        int index = value - 1;
        if (nums[index] < 0) {
            result[count++] = value;
        } else {
            nums[index] = -nums[index];
        }
    }
    *returnSize = count;
    return result;
}
