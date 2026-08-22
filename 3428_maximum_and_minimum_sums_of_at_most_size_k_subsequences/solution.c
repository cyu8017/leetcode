// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minMaxSums(int* nums, int numsSize, int k) {
    const int mod = 1000000007;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int n = numsSize;
    int** C = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        C[i] = (int*)calloc(k, sizeof(int));
        C[i][0] = 1;
        for (int j = 1; j < k && j <= i; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int waysMax = 0, waysMin = 0;
        for (int j = 0; j < k && j <= i; j++) waysMax = (waysMax + C[i][j]) % mod;
        int right = n - i - 1;
        for (int j = 0; j < k && j <= right; j++) waysMin = (waysMin + C[right][j]) % mod;
        ans = (ans + (long long)nums[i] * waysMax % mod + (long long)nums[i] * waysMin % mod) % mod;
    }
    for (int i = 0; i <= n; i++) free(C[i]);
    free(C);
    return ans;
}
