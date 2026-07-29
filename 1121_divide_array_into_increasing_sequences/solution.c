// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

#include <stdbool.h>

bool canDivideIntoSubsequences(int* nums, int numsSize, int k) {
    int maxCount = 0, cur = 0, prev = nums[0] - 1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == prev) cur++;
        else { cur = 1; prev = nums[i]; }
        if (cur > maxCount) maxCount = cur;
    }
    return numsSize >= k * maxCount;
}
