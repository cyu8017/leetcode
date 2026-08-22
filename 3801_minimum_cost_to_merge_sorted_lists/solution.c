// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

#include <stdlib.h>
#include <string.h>

long long minMergeCost(int** lists, int listsSize, int* listsColSize) {
    int m = listsSize;
    int totalMasks = 1 << m;
    int** merged = (int**)calloc((size_t)totalMasks, sizeof(int*));
    int* length = (int*)calloc((size_t)totalMasks, sizeof(int));
    int* median = (int*)calloc((size_t)totalMasks, sizeof(int));
    int* mcap = (int*)calloc((size_t)totalMasks, sizeof(int));
    for (int mask = 1; mask < totalMasks; mask++) {
        int bit = mask & -mask;
        int index = 0;
        while ((1 << index) != bit) index++;
        int* previous = merged[mask ^ bit];
        int prevLen = length[mask ^ bit];
        int* current = lists[index];
        int curLen = listsColSize[index];
        int outLen = prevLen + curLen;
        int* out = (int*)malloc((size_t)outLen * sizeof(int));
        int i = 0, j = 0, k = 0;
        while (i < prevLen || j < curLen) {
            if (j == curLen || (i < prevLen && previous[i] <= current[j])) out[k++] = previous[i++];
            else out[k++] = current[j++];
        }
        merged[mask] = out;
        length[mask] = outLen;
        median[mask] = out[(outLen - 1) / 2];
        (void)mcap;
    }
    const long long inf = 1LL << 62;
    long long* dp = (long long*)calloc((size_t)totalMasks, sizeof(long long));
    for (int mask = 1; mask < totalMasks; mask++) {
        if ((mask & (mask - 1)) == 0) continue;
        dp[mask] = inf;
        int firstBit = mask & -mask;
        for (int left = (mask - 1) & mask; left > 0; left = (left - 1) & mask) {
            if ((left & firstBit) == 0) continue;
            int right = mask ^ left;
            if (right == 0) continue;
            long long diff = median[left] - median[right];
            if (diff < 0) diff = -diff;
            long long candidate = dp[left] + dp[right] + length[mask] + diff;
            if (candidate < dp[mask]) dp[mask] = candidate;
        }
    }
    long long ans = dp[totalMasks - 1];
    for (int i = 0; i < totalMasks; i++) free(merged[i]);
    free(merged); free(length); free(median); free(mcap); free(dp);
    return ans;
}
