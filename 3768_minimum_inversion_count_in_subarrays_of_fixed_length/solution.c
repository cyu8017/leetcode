// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}
static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

static void bitAdd(int* bit, int n, int i, int d) {
    for (; i <= n; i += i & -i) bit[i] += d;
}
static int bitSum(int* bit, int i) {
    int r = 0;
    for (; i > 0; i -= i & -i) r += bit[i];
    return r;
}

long long minInversionCount(int* nums, int numsSize, int k) {
    int* vals = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(vals, nums, (size_t)numsSize * sizeof(int));
    qsort(vals, (size_t)numsSize, sizeof(int), cmpInt);
    int un = 0;
    for (int i = 0; i < numsSize; i++) {
        if (un == 0 || vals[un - 1] != vals[i]) vals[un++] = vals[i];
    }
    int* bit = (int*)calloc((size_t)(un + 1), sizeof(int));
    int* rank = (int*)malloc((size_t)numsSize * sizeof(int));
    long long inv = 0;
    for (int i = 0; i < numsSize; i++) {
        rank[i] = lowerBound(vals, un, nums[i]) + 1;
        if (i < k) {
            inv += i - bitSum(bit, rank[i]);
            bitAdd(bit, un, rank[i], 1);
        }
    }
    long long best = inv;
    for (int r = k; r < numsSize; r++) {
        int left = rank[r - k];
        inv -= bitSum(bit, left - 1);
        bitAdd(bit, un, left, -1);
        inv += (k - 1 - bitSum(bit, rank[r]));
        bitAdd(bit, un, rank[r], 1);
        if (inv < best) best = inv;
    }
    free(vals); free(bit); free(rank);
    return best;
}
