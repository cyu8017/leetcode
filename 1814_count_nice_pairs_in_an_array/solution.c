// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

#include <stdlib.h>

static int rev(int x) {
    int r = 0;
    while (x) {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r;
}

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int countNicePairs(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int* diffs = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) diffs[i] = nums[i] - rev(nums[i]);
    qsort(diffs, (size_t)numsSize, sizeof(int), cmpInt);

    long long ans = 0;
    int i = 0;
    while (i < numsSize) {
        int j = i;
        while (j < numsSize && diffs[j] == diffs[i]) j++;
        long long c = j - i;
        ans = (ans + c * (c - 1) / 2) % MOD;
        i = j;
    }
    free(diffs);
    return (int)ans;
}
