// LeetCode 0334 - Increasing Triplet Subsequence
// https://leetcode.com/problems/increasing-triplet-subsequence/

#include <limits.h>
#include <stdbool.h>

bool increasingTriplet(int* nums, int numsSize) {
    int first = INT_MAX;
    int second = INT_MAX;
    for (int index = 0; index < numsSize; index++) {
        int num = nums[index];
        if (num <= first) {
            first = num;
        } else if (num <= second) {
            second = num;
        } else {
            return true;
        }
    }
    return false;
}
