// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

#include <stdbool.h>

bool isArraySpecial(int* nums, int numsSize) {
    for (int i = 1; i < numsSize; i++)
        if (nums[i] % 2 == nums[i - 1] % 2) return false;
    return true;
}
