// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

#include <stdlib.h>

long long minSumSquareDiff(int* nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2) {
    (void)nums2Size;
    int n = nums1Size;
    int* diff = (int*)malloc((size_t)n * sizeof(int));
    int maxD = 0;
    for (int i = 0; i < n; i++) {
        int d = nums1[i] - nums2[i];
        if (d < 0) d = -d;
        diff[i] = d;
        if (d > maxD) maxD = d;
    }
    int k = k1 + k2;
    int* freq = (int*)calloc((size_t)(maxD + 1), sizeof(int));
    for (int i = 0; i < n; i++) freq[diff[i]]++;
    free(diff);
    for (int d = maxD; d > 0 && k > 0; d--) {
        if (freq[d] == 0) continue;
        int take = freq[d];
        if (take > k) take = k;
        freq[d] -= take;
        freq[d - 1] += take;
        k -= take;
    }
    long long ans = 0;
    for (int d = 0; d <= maxD; d++) {
        ans += (long long)d * d * freq[d];
    }
    free(freq);
    return ans;
}
