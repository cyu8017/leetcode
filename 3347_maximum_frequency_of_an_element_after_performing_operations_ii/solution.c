// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] < x) lo = mid + 1; else hi = mid; }
    return lo;
}
static int upper_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] <= x) lo = mid + 1; else hi = mid; }
    return lo;
}

int maxFrequency(int* nums, int numsSize, int k, int numOperations) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int n = numsSize, m = 0;
    int* keys = (int*)malloc(n * sizeof(int));
    int* freqs = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ) {
        int j = i; while (j < n && nums[j] == nums[i]) j++;
        keys[m] = nums[i]; freqs[m] = j - i; m++; i = j;
    }
    int* cand = (int*)malloc(3LL * n * sizeof(int));
    int cn = 0;
    for (int i = 0; i < n; i++) {
        cand[cn++] = nums[i] - k; cand[cn++] = nums[i]; cand[cn++] = nums[i] + k;
    }
    qsort(cand, cn, sizeof(int), cmp_int);
    int ans = 1;
    for (int i = 0; i < cn; i++) {
        if (i && cand[i] == cand[i - 1]) continue;
        int t = cand[i];
        int can = upper_bound(nums, n, t + k) - lower_bound(nums, n, t - k);
        int f = 0, pos = lower_bound(keys, m, t);
        if (pos < m && keys[pos] == t) f = freqs[pos];
        int use = can < f + numOperations ? can : f + numOperations;
        if (use > ans) ans = use;
    }
    free(keys); free(freqs); free(cand);
    return ans;
}
