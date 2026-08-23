// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

#include <stdint.h>

static int64_t gcd4010(int64_t a, int64_t b) {
    while (b) {
        int64_t t = a % b;
        a = b;
        b = t;
    }
    return a;
}

long long maxPairStrength(int* nums, int numsSize) {
    int64_t ans = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            int64_t g = gcd4010((int64_t)nums[i], (int64_t)nums[j]);
            int64_t x = (int64_t)nums[i] * (int64_t)nums[j] / (g * g);
            if (x > ans) ans = x;
        }
    }
    return ans;
}
