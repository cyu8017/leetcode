// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

#include <stdbool.h>

bool hasTrailingZeros(int* nums, int numsSize) {
    int even = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) {
            even++;
            if (even >= 2) return true;
        }
    }
    return false;
}
