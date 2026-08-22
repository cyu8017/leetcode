// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

#include <stdbool.h>
#include <string.h>

int distinctPrimeFactors(int* nums, int numsSize) {
    bool set[1001] = {0};
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (int p = 2; p * p <= x; p++) {
            if (x % p == 0) {
                set[p] = true;
                while (x % p == 0) x /= p;
            }
        }
        if (x > 1) set[x] = true;
    }
    int ans = 0;
    for (int i = 0; i <= 1000; i++) if (set[i]) ans++;
    return ans;
}
