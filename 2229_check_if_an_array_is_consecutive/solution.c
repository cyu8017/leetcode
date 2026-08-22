// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isConsecutive(int* nums, int numsSize) {
    int mn = nums[0], mx = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    if (mx - mn + 1 != numsSize) return false;
    bool* seen = (bool*)calloc((size_t)numsSize, sizeof(bool));
    for (int i = 0; i < numsSize; i++) {
        int idx = nums[i] - mn;
        if (seen[idx]) { free(seen); return false; }
        seen[idx] = true;
    }
    free(seen);
    return true;
}
