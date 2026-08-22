// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

#include <stdlib.h>
#include <string.h>

int maximumANDSum(int* nums, int numsSize, int numSlots) {
    int n = numsSize, slots = numSlots;
    int maxMask = 1;
    for (int i = 0; i < slots; i++) maxMask *= 3;
    int* dp = (int*)calloc((size_t)maxMask, sizeof(int));
    for (int mask = 0; mask < maxMask; mask++) {
        int cnt = 0, x = mask;
        while (x) { cnt += x % 3; x /= 3; }
        if (cnt >= n) continue;
        int v = nums[cnt], base = 1;
        for (int s = 1; s <= slots; s++) {
            int occ = (mask / base) % 3;
            if (occ < 2) {
                int nm = mask + base;
                int cand = dp[mask] + (v & s);
                if (cand > dp[nm]) dp[nm] = cand;
            }
            base *= 3;
        }
    }
    int ans = 0;
    for (int i = 0; i < maxMask; i++) if (dp[i] > ans) ans = dp[i];
    free(dp);
    return ans;
}
