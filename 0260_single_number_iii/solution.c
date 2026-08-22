// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

#include <stdlib.h>

int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int xorAll = 0;
    for (int i = 0; i < numsSize; i++) {
        xorAll ^= nums[i];
    }
    int diff = xorAll & -xorAll;
    int first = 0;
    int second = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] & diff) {
            first ^= nums[i];
        } else {
            second ^= nums[i];
        }
    }
    int* result = malloc(2 * sizeof(int));
    result[0] = first;
    result[1] = second;
    *returnSize = 2;
    return result;
}
