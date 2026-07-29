// LeetCode 1929 - Concatenation of Array
// https://leetcode.com/problems/concatenation-of-array/

#include <stdlib.h>
#include <string.h>

int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* res = (int*)malloc((size_t)numsSize * 2 * sizeof(int));
    memcpy(res, nums, (size_t)numsSize * sizeof(int));
    memcpy(res + numsSize, nums, (size_t)numsSize * sizeof(int));
    *returnSize = numsSize * 2;
    return res;
}
