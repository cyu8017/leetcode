// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

#include <stdlib.h>
#include <stdbool.h>

static int findp(int* parent, int x) {
    if (parent[x] != x) parent[x] = findp(parent, parent[x]);
    return parent[x];
}

long long* maximumSegmentSum(int* nums, int numsSize, int* removeQueries, int removeQueriesSize, int* returnSize) {
    (void)removeQueriesSize;
    int n = numsSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    long long* sum = (long long*)calloc((size_t)n, sizeof(long long));
    bool* active = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < n; i++) parent[i] = i;
    long long* ans = (long long*)malloc((size_t)n * sizeof(long long));
    long long best = 0;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] = best;
        int idx = removeQueries[i];
        active[idx] = true;
        sum[idx] = nums[idx];
        if (idx > 0 && active[idx - 1]) {
            int ra = findp(parent, idx), rb = findp(parent, idx - 1);
            if (ra != rb) { parent[rb] = ra; sum[ra] += sum[rb]; }
        }
        if (idx + 1 < n && active[idx + 1]) {
            int ra = findp(parent, idx), rb = findp(parent, idx + 1);
            if (ra != rb) { parent[rb] = ra; sum[ra] += sum[rb]; }
        }
        long long s = sum[findp(parent, idx)];
        if (s > best) best = s;
    }
    free(parent); free(sum); free(active);
    *returnSize = n;
    return ans;
}
