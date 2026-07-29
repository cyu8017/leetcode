// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

#include <stdlib.h>
#include <limits.h>

int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    long long NEG = LLONG_MIN / 4;
    long long* dp = (long long*)malloc((nums2Size + 1) * sizeof(long long));
    for (int j = 0; j <= nums2Size; j++) dp[j] = NEG;
    for (int i = 0; i < nums1Size; i++) {
        long long* prev = (long long*)malloc((nums2Size + 1) * sizeof(long long));
        for (int j = 0; j <= nums2Size; j++) prev[j] = dp[j];
        for (int j = 1; j <= nums2Size; j++) {
            long long product = (long long)nums1[i] * nums2[j - 1];
            long long best = product;
            if (dp[j - 1] > best) best = dp[j - 1];
            if (prev[j] > best) best = prev[j];
            long long with = product + (prev[j - 1] > 0 ? prev[j - 1] : 0);
            if (with > best) best = with;
            dp[j] = best;
        }
        free(prev);
    }
    int ans = (int)dp[nums2Size];
    free(dp);
    return ans;
}
