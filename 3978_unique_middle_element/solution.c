// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

#include <stdbool.h>

bool isMiddleElementUnique(int* nums, int numsSize) {
    int mid = nums[numsSize / 2];
    int cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == mid) cnt++;
    }
    return cnt == 1;
}
