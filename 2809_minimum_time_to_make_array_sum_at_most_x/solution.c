// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

#include <stdlib.h>

typedef struct { int a, b; } Pair2809;
static int cmp2809(const void* a, const void* b) {
    return ((const Pair2809*)a)->b - ((const Pair2809*)b)->b;
}

int minimumTime(int* nums1, int nums1Size, int* nums2, int nums2Size, int x) {
    (void)nums2Size;
    int n = nums1Size;
    Pair2809* arr = (Pair2809*)malloc(n * sizeof(Pair2809));
    long long sum1 = 0, sum2 = 0;
    for (int i = 0; i < n; i++) {
        arr[i].a = nums1[i]; arr[i].b = nums2[i];
        sum1 += nums1[i]; sum2 += nums2[i];
    }
    qsort(arr, n, sizeof(Pair2809), cmp2809);
    int* dp = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j >= 1; j--) {
            int cand = dp[j - 1] + arr[i].a + j * arr[i].b;
            if (cand > dp[j]) dp[j] = cand;
        }
    }
    for (int t = 0; t <= n; t++) {
        if (sum1 + sum2 * t - dp[t] <= x) {
            free(arr); free(dp);
            return t;
        }
    }
    free(arr); free(dp);
    return -1;
}
