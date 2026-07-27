// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int twoSumLessThanK(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int lo = 0, hi = numsSize - 1, ans = -1;
    while (lo < hi) {
        int total = nums[lo] + nums[hi];
        if (total < k) {
            if (total > ans) {
                ans = total;
            }
            lo++;
        } else {
            hi--;
        }
    }
    return ans;
}
