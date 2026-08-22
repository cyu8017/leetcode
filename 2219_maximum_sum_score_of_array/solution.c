// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

#include <limits.h>

long long maximumSumScore(int* nums, int numsSize) {
    long long total = 0, pref = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    long long ans = LLONG_MIN;
    for (int i = 0; i < numsSize; i++) {
        pref += nums[i];
        long long score = pref;
        long long other = total - pref + nums[i];
        if (other > score) score = other;
        if (score > ans) ans = score;
    }
    return ans;
}
