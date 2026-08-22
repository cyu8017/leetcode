// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

int maximumStrongPairXor(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (int j = i; j < numsSize && nums[j] <= 2 * x; j++) {
            int xorr = x ^ nums[j];
            if (xorr > ans) ans = xorr;
        }
    }
    return ans;
}
