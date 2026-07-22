// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

#include <stdlib.h>

static void lisLens(int* a, int n, int* out) {
    int* d = (int*)malloc((size_t)n * sizeof(int));
    int dsz = 0;
    for (int i = 0; i < n; i++) {
        int lo = 0, hi = dsz;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (d[mid] < a[i]) lo = mid + 1;
            else hi = mid;
        }
        if (lo == dsz) d[dsz++] = a[i];
        else d[lo] = a[i];
        out[i] = lo + 1;
    }
    free(d);
}

int minimumMountainRemovals(int* nums, int numsSize) {
    int n = numsSize;
    int* L = (int*)malloc((size_t)n * sizeof(int));
    int* R = (int*)malloc((size_t)n * sizeof(int));
    int* rev = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) rev[i] = nums[n - 1 - i];
    lisLens(nums, n, L);
    int* Rt = (int*)malloc((size_t)n * sizeof(int));
    lisLens(rev, n, Rt);
    for (int i = 0; i < n; i++) R[i] = Rt[n - 1 - i];
    int best = 0;
    for (int i = 0; i < n; i++) {
        if (L[i] > 1 && R[i] > 1) {
            int len = L[i] + R[i] - 1;
            if (len > best) best = len;
        }
    }
    free(L); free(R); free(rev); free(Rt);
    return n - best;
}
