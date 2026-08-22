// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool canSubsetSum(int* vals, int n, int target) {
    if (target == 0) return true;
    bool* dp = (bool*)calloc((size_t)target + 1, sizeof(bool));
    dp[0] = true;
    for (int i = 0; i < n; i++) {
        int v = vals[i];
        for (int s = target; s >= v; s--) {
            if (dp[s - v]) dp[s] = true;
        }
    }
    bool ok = dp[target];
    free(dp);
    return ok;
}

static bool okK(int* nums, int n, int** queries, int k) {
    for (int i = 0; i < n; i++) {
        if (nums[i] == 0) continue;
        int* vals = (int*)malloc((size_t)k * sizeof(int));
        int vc = 0;
        for (int q = 0; q < k; q++) {
            int l = queries[q][0], r = queries[q][1], v = queries[q][2];
            if (l <= i && i <= r) vals[vc++] = v;
        }
        if (!canSubsetSum(vals, vc, nums[i])) {
            free(vals);
            return false;
        }
        free(vals);
    }
    return true;
}

int minZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    if (okK(nums, numsSize, queries, 0)) return 0;
    int lo = 1, hi = queriesSize + 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (mid <= queriesSize && okK(nums, numsSize, queries, mid)) hi = mid;
        else lo = mid + 1;
    }
    if (lo > queriesSize) return -1;
    return lo;
}
