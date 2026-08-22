// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solveQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    int n = numsSize;
    /* nums[i] in [1, 1e6] typically - use lists via scanning */
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int idx = queries[qi];
        int x = nums[idx];
        int best = n;
        int cnt = 0;
        for (int p = 0; p < n; p++) {
            if (nums[p] != x) continue;
            cnt++;
            if (p == idx) continue;
            int d = p - idx;
            if (d < 0) d = -d;
            int d2 = n - d;
            if (d2 < d) d = d2;
            if (d < best) best = d;
        }
        ans[qi] = (cnt == 1) ? -1 : best;
    }
    *returnSize = queriesSize;
    return ans;
}
