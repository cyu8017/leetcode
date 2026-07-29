// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minDifference(int* nums, int numsSize) {
    if (numsSize <= 4) return 0;
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int ans = nums[numsSize - 1] - nums[0];
    for (int i = 0; i < 4; i++) {
        int diff = nums[numsSize - 4 + i] - nums[i];
        if (diff < ans) ans = diff;
    }
    return ans;
}
