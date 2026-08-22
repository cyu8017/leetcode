// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

#include <stdbool.h>

bool canAliceWin(int* nums, int numsSize) {
    int a = 0, b = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < 10) a += nums[i];
        else b += nums[i];
    }
    return a != b;
}
