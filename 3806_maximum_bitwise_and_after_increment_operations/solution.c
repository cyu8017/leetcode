// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

#include <stdlib.h>

static int bit_len(unsigned int x) {
    int n = 0;
    while (x) { n++; x >>= 1; }
    return n;
}

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumAND(int* nums, int numsSize, int k, int m) {
    int mxVal = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mxVal) mxVal = nums[i];
    int mx = bit_len((unsigned int)(mxVal + k));
    int ans = 0;
    int* cost = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int bit = mx - 1; bit >= 0; bit--) {
        int target = ans | (1 << bit);
        for (int i = 0; i < numsSize; i++) {
            int x = nums[i];
            int j = bit_len((unsigned int)(target & ~x));
            int mask = (1 << j) - 1;
            cost[i] = (target & mask) - (x & mask);
        }
        qsort(cost, (size_t)numsSize, sizeof(int), cmp_int);
        int sum = 0;
        for (int i = 0; i < m; i++) sum += cost[i];
        if (sum <= k) ans = target;
    }
    free(cost);
    return ans;
}
