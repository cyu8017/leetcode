// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

#include <stdint.h>

long long maximumAlternatingSubarraySum(int* nums, int numsSize) {
    long long ans = INT64_MIN;
    long long even = 0, odd = 0;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        if (i % 2 == 0) even += x;
        else {
            if (even - x > 0) even = even - x;
            else even = 0;
        }
        if (even > ans) ans = even;
    }
    even = 0;
    for (int i = 1; i < numsSize; i++) {
        long long x = nums[i];
        if (i % 2 == 1) odd += x;
        else {
            if (odd - x > 0) odd = odd - x;
            else odd = 0;
        }
        if (odd > ans) ans = odd;
    }
    (void)even;
    return ans;
}
