// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

#include <stdbool.h>

bool checkPossibility(int* nums, int numsSize) {
    int changes = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[i - 1]) {
            if (++changes > 1) return false;
            if (i >= 2 && nums[i] < nums[i - 2]) nums[i] = nums[i - 1];
            else nums[i - 1] = nums[i];
        }
    }
    return true;
}
