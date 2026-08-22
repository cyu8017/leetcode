// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

#include <stdlib.h>

// JavaScript problem; C stand-in: last int element or -1.
int last(int* nums, int numsSize) {
    if (numsSize == 0) return -1;
    return nums[numsSize - 1];
}
