// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

bool canDistribute(int* nums, int numsSize, int* quantity, int quantitySize) {
    int* freqMap = (int*)calloc(1001, sizeof(int));
    for (int i = 0; i < numsSize; i++) freqMap[nums[i]]++;
    int cnt[1001], cntN = 0;
    for (int i = 0; i <= 1000; i++) if (freqMap[i]) cnt[cntN++] = freqMap[i];
    free(freqMap);
    qsort(quantity, (size_t)quantitySize, sizeof(int), cmpDesc);
    int m = quantitySize;
    int full = (1 << m) - 1;
    int* sums = (int*)calloc((size_t)(1 << m), sizeof(int));
    for (int mask = 1; mask <= full; mask++) {
        int bit = mask & -mask;
        int idx = 0;
        while ((1 << idx) != bit) idx++;
        sums[mask] = sums[mask ^ bit] + quantity[idx];
    }
    bool* dp = (bool*)calloc((size_t)(1 << m), sizeof(bool));
    bool* nxt = (bool*)calloc((size_t)(1 << m), sizeof(bool));
    dp[0] = true;
    for (int ci = 0; ci < cntN; ci++) {
        int c = cnt[ci];
        memcpy(nxt, dp, (size_t)(1 << m) * sizeof(bool));
        for (int mask = 0; mask <= full; mask++) {
            if (!dp[mask]) continue;
            int left = full ^ mask;
            for (int sub = left; sub; sub = (sub - 1) & left) {
                if (sums[sub] <= c) nxt[mask | sub] = true;
            }
        }
        memcpy(dp, nxt, (size_t)(1 << m) * sizeof(bool));
    }
    bool ok = dp[full];
    free(sums); free(dp); free(nxt);
    return ok;
}
