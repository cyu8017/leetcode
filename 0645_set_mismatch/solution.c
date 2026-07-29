// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

#include <stdlib.h>

int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int* seen = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    int dup = 0, missing = 0;
    for (int i = 0; i < numsSize; i++) {
        if (seen[nums[i]]) {
            dup = nums[i];
        }
        seen[nums[i]] = 1;
    }
    for (int i = 1; i <= numsSize; i++) {
        if (!seen[i]) {
            missing = i;
            break;
        }
    }
    free(seen);
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = dup;
    result[1] = missing;
    *returnSize = 2;
    return result;
}
