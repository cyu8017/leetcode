// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

#include <stdbool.h>

bool isMonotonic(int* nums, int numsSize) {
    bool inc = true, dec = true;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[i - 1]) inc = false;
        if (nums[i] > nums[i - 1]) dec = false;
    }
    return inc || dec;
}
