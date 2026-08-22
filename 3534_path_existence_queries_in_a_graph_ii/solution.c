// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

#include <stdlib.h>

typedef struct { int x, i; } P3534;
static int cmp_p(const void* a, const void* b) {
    return (((const P3534*)a)->x > ((const P3534*)b)->x) - (((const P3534*)a)->x < ((const P3534*)b)->x);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)numsSize; (void)queriesColSize;
    P3534* pairs = (P3534*)malloc((size_t)n * sizeof(P3534));
    for (int i = 0; i < n; i++) { pairs[i].x = nums[i]; pairs[i].i = i; }
    qsort(pairs, (size_t)n, sizeof(P3534), cmp_p);
    int m = 20;
    int** f = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) f[i] = (int*)calloc((size_t)m, sizeof(int));
    int r = n - 1;
    for (int l = n - 1; l >= 0; l--) {
        while (pairs[r].x - pairs[l].x > maxDiff) r--;
        int i = pairs[l].i, j = pairs[r].i;
        f[i][0] = j;
        for (int k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int i = queries[qi][0], j = queries[qi][1];
        if (nums[i] > nums[j]) { int t = i; i = j; j = t; }
        if (i == j) { ans[qi] = 0; continue; }
        if (nums[i] == nums[j]) { ans[qi] = 1; continue; }
        int d = 0;
        for (int k = m - 1; k >= 0; k--) {
            if (nums[f[i][k]] < nums[j]) { d |= 1 << k; i = f[i][k]; }
        }
        if (nums[f[i][0]] < nums[j]) ans[qi] = -1;
        else ans[qi] = d + 1;
    }
    for (int i = 0; i < n; i++) free(f[i]);
    free(f); free(pairs);
    *returnSize = queriesSize;
    return ans;
}
