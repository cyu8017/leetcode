// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

#include <stdlib.h>

static int* g_nums; static int g_n;
static int** g_queries; static int g_qsize;

static int ok3356(int k) {
    int* diff = (int*)calloc(g_n + 1, sizeof(int));
    for (int i = 0; i < k; i++) {
        diff[g_queries[i][0]] += g_queries[i][2];
        diff[g_queries[i][1] + 1] -= g_queries[i][2];
    }
    int cur = 0;
    for (int i = 0; i < g_n; i++) {
        cur += diff[i];
        if (cur < g_nums[i]) { free(diff); return 0; }
    }
    free(diff);
    return 1;
}

int minZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    g_nums = nums; g_n = numsSize; g_queries = queries; g_qsize = queriesSize;
    if (ok3356(0)) return 0;
    int lo = 1, hi = queriesSize + 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (mid <= queriesSize && ok3356(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo > queriesSize ? -1 : lo;
}
