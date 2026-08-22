// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int findMaxK(int* nums, int numsSize) {
    bool pos[1001] = {0}, neg[1001] = {0};
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > 0) pos[nums[i]] = true;
        else if (nums[i] < 0) neg[-nums[i]] = true;
    }
    for (int x = 1000; x >= 1; x--) {
        if (pos[x] && neg[x]) return x;
    }
    return -1;
}
