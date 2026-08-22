// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int absDiff(int a, int b) {
    return a >= b ? a - b : b - a;
}

int minAbsoluteSumDiff(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    const int MOD = 1000000007;
    int* sorted = (int*)malloc((size_t)nums1Size * sizeof(int));
    for (int i = 0; i < nums1Size; i++) sorted[i] = nums1[i];
    qsort(sorted, (size_t)nums1Size, sizeof(int), cmpInt);

    long long total = 0;
    int bestGain = 0;
    for (int i = 0; i < nums1Size; i++) {
        int current = absDiff(nums1[i], nums2[i]);
        total += current;

        int lo = 0, hi = nums1Size;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (sorted[mid] < nums2[i]) lo = mid + 1;
            else hi = mid;
        }
        for (int j = lo - 1; j <= lo; j++) {
            if (j >= 0 && j < nums1Size) {
                int gain = current - absDiff(sorted[j], nums2[i]);
                if (gain > bestGain) bestGain = gain;
            }
        }
    }
    free(sorted);
    return (int)((total - bestGain) % MOD);
}
