// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

#include <stdbool.h>

int thirdMax(int* nums, int numsSize) {
    bool hasFirst = false;
    bool hasSecond = false;
    bool hasThird = false;
    int first = 0;
    int second = 0;
    int third = 0;

    for (int index = 0; index < numsSize; index++) {
        int value = nums[index];
        if ((hasFirst && value == first) || (hasSecond && value == second) ||
            (hasThird && value == third)) {
            continue;
        }
        if (!hasFirst || value > first) {
            if (hasFirst) {
                third = second;
                hasThird = hasSecond;
            }
            if (hasSecond) {
                second = first;
                hasSecond = true;
            }
            first = value;
            hasFirst = true;
        } else if (!hasSecond || value > second) {
            if (hasSecond) {
                third = second;
                hasThird = true;
            }
            second = value;
            hasSecond = true;
        } else if (!hasThird || value > third) {
            third = value;
            hasThird = true;
        }
    }

    return hasThird ? third : first;
}
