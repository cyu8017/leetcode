// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

#include <stdbool.h>

static bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= n / i; i++) if (n % i == 0) return false;
    return true;
}

int maximumPrimeDifference(int* nums, int numsSize) {
    for (int i = 0; ; i++) {
        if (isPrime(nums[i])) {
            for (int j = numsSize - 1; ; j--) {
                if (isPrime(nums[j])) return j - i;
            }
        }
    }
}
