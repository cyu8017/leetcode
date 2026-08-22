// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static long long countLE(int* nums, int n, int x) {
    long long ans = 0;
    int l = 0, r = n - 1;
    while (l < r) {
        if (nums[l] + nums[r] <= x) { ans += r - l; l++; }
        else r--;
    }
    return ans;
}

long long countFairPairs(int* nums, int numsSize, int lower, int upper) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    return countLE(nums, numsSize, upper) - countLE(nums, numsSize, lower - 1);
}
