// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

#include <stdlib.h>

static int countInv(int* nums, int n, int k, int threshold) {
    int* sorted = (int*)malloc((size_t)n * sizeof(int));
    int sn = 0, inv = 0;
    for (int ti = 0; ti < n; ti++) {
        int num = nums[ti];
        int lo = 0, hi = sn;
        while (lo < hi) { int mid = (lo + hi) / 2; if (sorted[mid] <= num) lo = mid + 1; else hi = mid; }
        int left = lo;
        lo = 0; hi = sn;
        while (lo < hi) { int mid = (lo + hi) / 2; if (sorted[mid] <= num + threshold) lo = mid + 1; else hi = mid; }
        inv += lo - left;
        lo = 0; hi = sn;
        while (lo < hi) { int mid = (lo + hi) / 2; if (sorted[mid] < num) lo = mid + 1; else hi = mid; }
        for (int i = sn; i > lo; i--) sorted[i] = sorted[i - 1];
        sorted[lo] = num;
        sn++;
        if (inv >= k) { free(sorted); return 1; }
    }
    free(sorted);
    return inv >= k;
}

int minThreshold(int* nums, int numsSize, int k) {
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int l = 0, r = mx + 1;
    while (l < r) {
        int m = (l + r) / 2;
        if (countInv(nums, numsSize, k, m)) r = m;
        else l = m + 1;
    }
    if (l > mx) return -1;
    return l;
}
