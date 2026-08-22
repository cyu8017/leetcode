// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

#include <stdlib.h>

static int* g_nums;
static int cmp_idx(const void* a, const void* b) {
    return g_nums[*(const int*)a] - g_nums[*(const int*)b];
}
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

int* lexicographicallySmallestArray(int* nums, int numsSize, int limit, int* returnSize) {
    int n = numsSize;
    g_nums = nums;
    int* idx = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) idx[i] = i;
    qsort(idx, n, sizeof(int), cmp_idx);
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ) {
        int j = i + 1;
        while (j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit) j++;
        int* groupIdx = (int*)malloc((j - i) * sizeof(int));
        int* vals = (int*)malloc((j - i) * sizeof(int));
        for (int t = i; t < j; t++) { groupIdx[t - i] = idx[t]; vals[t - i] = nums[idx[t]]; }
        qsort(groupIdx, j - i, sizeof(int), cmp_int);
        for (int t = 0; t < j - i; t++) ans[groupIdx[t]] = vals[t];
        free(groupIdx); free(vals);
        i = j;
    }
    free(idx);
    *returnSize = n;
    return ans;
}
