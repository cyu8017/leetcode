// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

#include <stdlib.h>

int* minDifference(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int (*pref)[101] = calloc((size_t)numsSize + 1, sizeof(*pref));
    for (int i = 0; i < numsSize; i++) {
        for (int v = 0; v <= 100; v++) pref[i + 1][v] = pref[i][v];
        pref[i + 1][nums[i]]++;
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int left = queries[q][0], right = queries[q][1];
        int prev = -1, best = 101;
        for (int value = 1; value <= 100; value++) {
            if (pref[right + 1][value] - pref[left][value] > 0) {
                if (prev != -1 && value - prev < best) best = value - prev;
                prev = value;
            }
        }
        ans[q] = best == 101 ? -1 : best;
    }
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
