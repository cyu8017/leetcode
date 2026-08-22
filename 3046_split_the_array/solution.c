// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

#include <stdbool.h>

bool isPossibleToSplit(int* nums, int numsSize) {
    int cnt[101] = {0};
    for (int i = 0; i < numsSize; i++) {
        if (++cnt[nums[i]] >= 3) return false;
    }
    return true;
}
