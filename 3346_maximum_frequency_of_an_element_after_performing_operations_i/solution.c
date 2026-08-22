// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

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
    int ans = 1;
    for (int i = 0; i < m; i++) {
        int t = keys[i], f = freqs[i];
        int can = upper_bound(nums, n, t + k) - lower_bound(nums, n, t - k);
        int use = can < f + numOperations ? can : f + numOperations;
        if (use > ans) ans = use;
    }
    for (int l = 0, r = 0; r < n; r++) {
        while (nums[r] - nums[l] > 2 * k) l++;
        int window = r - l + 1;
        if (window > numOperations) window = numOperations;
        if (window > ans) ans = window;
    }
    free(keys); free(freqs);
    return ans;
}
