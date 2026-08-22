// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimizeSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int a = nums[numsSize - 1] - nums[2];
    int b = nums[numsSize - 3] - nums[0];
    int c = nums[numsSize - 2] - nums[1];
    int ans = a;
    if (b < ans) ans = b;
    if (c < ans) ans = c;
    return ans;
}
