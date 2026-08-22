// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

#include <stdlib.h>

static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countStableSubarrays(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = numsSize;
    int* seg = (int*)malloc((size_t)n * sizeof(int));
    long long* s = (long long*)malloc((size_t)(n + 2) * sizeof(long long));
    int sn = 0;
    s[0] = 0;
    int l = 0;
    for (int r = 0; r < n; r++) {
        if (r == n - 1 || nums[r] > nums[r + 1]) {
            seg[sn] = l;
            long long k = r - l + 1;
            s[sn + 1] = s[sn] + k * (k + 1) / 2;
            sn++;
            l = r + 1;
        }
    }
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    for (int idx = 0; idx < queriesSize; idx++) {
        int left = queries[idx][0], right = queries[idx][1];
        int i = lowerBound(seg, sn, left + 1);
        int j = lowerBound(seg, sn, right + 1) - 1;
        if (i > j) {
            long long k = right - left + 1;
            ans[idx] = k * (k + 1) / 2;
        } else {
            long long a = seg[i] - left;
            long long b = right - seg[j] + 1;
            ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2;
        }
    }
    free(seg); free(s);
    *returnSize = queriesSize;
    return ans;
}
