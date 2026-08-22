// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

#include <stdbool.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)numsSize; (void)queriesColSize;
    int* g = (int*)calloc((size_t)n, sizeof(int));
    int cnt = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) cnt++;
        g[i] = cnt;
    }
    bool* ans = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = g[queries[i][0]] == g[queries[i][1]];
    }
    free(g);
    *returnSize = queriesSize;
    return ans;
}
