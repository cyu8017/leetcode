// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

#include <stdlib.h>
#include <limits.h>

long long maximumScore(int* nums, int numsSize) {
    int n = numsSize;
    long long* suf = (long long*)malloc((size_t)n * sizeof(long long));
    suf[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        long long v = nums[i];
        suf[i] = v < suf[i + 1] ? v : suf[i + 1];
    }
    long long pre = 0;
    long long ans = LLONG_MIN;
    for (int i = 0; i < n - 1; i++) {
        pre += nums[i];
        long long cand = pre - suf[i + 1];
        if (cand > ans) ans = cand;
    }
    free(suf);
    return ans;
}
