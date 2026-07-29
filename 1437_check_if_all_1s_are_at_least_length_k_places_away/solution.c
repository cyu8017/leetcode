// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

#include <stdbool.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int previous = -k - 1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i]) {
            if (i - previous <= k) return false;
            previous = i;
        }
    }
    return true;
}
