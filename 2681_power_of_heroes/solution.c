// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

#include <stdlib.h>

static int cmpInt2681(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int sumOfPower(int* nums, int numsSize) {
    const int MOD = 1000000007;
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt2681);
    long long ans = 0, s = 0;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        ans = (ans + x * x % MOD * (s + x) % MOD) % MOD;
        s = (2 * s + x) % MOD;
    }
    return (int)ans;
}
