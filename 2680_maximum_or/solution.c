// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

#include <stdlib.h>

long long maximumOr(int* nums, int numsSize, int k) {
    int* suf = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    for (int i = numsSize - 1; i >= 0; i--)
        suf[i] = suf[i + 1] | nums[i];
    long long pref = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        long long cand = pref | ((long long)nums[i] << k) | (long long)suf[i + 1];
        if (cand > ans) ans = cand;
        pref |= (long long)nums[i];
    }
    free(suf);
    return ans;
}
