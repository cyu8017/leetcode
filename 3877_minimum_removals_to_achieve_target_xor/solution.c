// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

#include <stdlib.h>
#include <limits.h>

static int bitLen3877(unsigned x) {
    int n = 0;
    while (x) { n++; x >>= 1; }
    return n;
}

int minRemovals(int* nums, int numsSize, int target) {
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int m = bitLen3877((unsigned)mx);
    if ((1 << m) <= target) return -1;
    int width = 1 << m;
    int n = numsSize;
    int* prev = (int*)malloc((size_t)width * sizeof(int));
    int* cur = (int*)malloc((size_t)width * sizeof(int));
    for (int j = 0; j < width; j++) prev[j] = INT_MIN;
    prev[0] = 0;
    for (int i = 1; i <= n; i++) {
        int x = nums[i - 1];
        for (int j = 0; j < width; j++) {
            int a = prev[j];
            int b = prev[j ^ x];
            if (b != INT_MIN) b = b + 1;
            cur[j] = a > b ? a : b;
        }
        int* tmp = prev; prev = cur; cur = tmp;
    }
    int ans = prev[target] < 0 ? -1 : n - prev[target];
    free(prev); free(cur);
    return ans;
}
