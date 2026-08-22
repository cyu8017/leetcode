// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

#include <stdbool.h>

bool canSplitArray(int* nums, int numsSize, int m) {
    if (numsSize <= 2) return true;
    for (int i = 0; i + 1 < numsSize; i++) {
        if (nums[i] + nums[i + 1] >= m) return true;
    }
    return false;
}
