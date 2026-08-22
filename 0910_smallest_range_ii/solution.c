// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int smallestRangeII(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int ans = nums[numsSize - 1] - nums[0];
    for (int i = 0; i < numsSize - 1; i++) {
        int lo = nums[0] + k < nums[i + 1] - k ? nums[0] + k : nums[i + 1] - k;
        int hi = nums[numsSize - 1] - k > nums[i] + k ? nums[numsSize - 1] - k : nums[i] + k;
        if (hi - lo < ans) ans = hi - lo;
    }
    return ans;
}
