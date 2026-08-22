// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

#include <stdlib.h>

long long maxProduct(int* nums, int numsSize) {
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    int bitsN = 0;
    for (int x = maxV; x > 0; x >>= 1) bitsN++;
    if (bitsN == 0) bitsN = 1;
    int size = 1 << bitsN;
    int* best = (int*)calloc((size_t)size, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        if (v > best[v]) best[v] = v;
    }
    for (int mask = 0; mask < size; mask++) {
        for (int b = 0; b < bitsN; b++) {
            if (mask & (1 << b)) {
                int sub = mask ^ (1 << b);
                if (best[sub] > best[mask]) best[mask] = best[sub];
            }
        }
    }
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        int comp = (size - 1) ^ v;
        if (best[comp] > 0) {
            long long p = (long long)v * best[comp];
            if (p > ans) ans = p;
        }
    }
    free(best);
    return ans;
}
