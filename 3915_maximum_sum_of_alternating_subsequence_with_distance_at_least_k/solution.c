// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

#include <stdlib.h>
#include <string.h>

static long long maxll3915(long long a, long long b) { return a > b ? a : b; }

static void fenwickUpd3915(long long* f, int n, int i, long long val) {
    for (; i < n; i += i & -i) if (val > f[i]) f[i] = val;
}
static long long fenwickPreMax3915(long long* f, int i) {
    long long res = 0;
    for (; i > 0; i &= i - 1) if (f[i] > res) res = f[i];
    return res;
}
static int cmpInt3915(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxAlternatingSum(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* sorted = malloc((size_t)n * sizeof(int));
    memcpy(sorted, nums, (size_t)n * sizeof(int));
    qsort(sorted, (size_t)n, sizeof(int), cmpInt3915);
    int m = 0;
    if (n) {
        m = 1;
        for (int i = 1; i < n; i++) if (sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
    }
    long long* fInc = calloc((size_t)n, sizeof(long long));
    long long* fDec = calloc((size_t)n, sizeof(long long));
    long long* inc = calloc((size_t)(m + 1), sizeof(long long));
    long long* dec = calloc((size_t)(m + 1), sizeof(long long));
    int* ranks = malloc((size_t)n * sizeof(int));
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        if (i >= k) {
            int j = ranks[i - k];
            fenwickUpd3915(inc, m + 1, m - j, fInc[i - k]);
            fenwickUpd3915(dec, m + 1, j + 1, fDec[i - k]);
        }
        int lo = 0, hi = m;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (sorted[mid] >= x) hi = mid;
            else lo = mid + 1;
        }
        int j = lo;
        ranks[i] = j;
        fInc[i] = fenwickPreMax3915(dec, j) + x;
        fDec[i] = fenwickPreMax3915(inc, m - 1 - j) + x;
        ans = maxll3915(ans, maxll3915(fInc[i], fDec[i]));
    }
    free(sorted); free(fInc); free(fDec); free(inc); free(dec); free(ranks);
    return ans;
}
