// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

#include <stdbool.h>

bool check(int* nums, int numsSize) {
    int drops = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > nums[(i + 1) % numsSize]) {
            drops++;
        }
    }
    return drops <= 1;
}
