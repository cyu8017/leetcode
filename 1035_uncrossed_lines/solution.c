// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

#include <stdlib.h>

int maxUncrossedLines(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int m = nums1Size, n = nums2Size;
    int* dp = (int*)calloc((size_t)(m + 1) * (n + 1), sizeof(int));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (nums1[i - 1] == nums2[j - 1])
                dp[i * (n + 1) + j] = dp[(i - 1) * (n + 1) + (j - 1)] + 1;
            else {
                int a = dp[(i - 1) * (n + 1) + j];
                int b = dp[i * (n + 1) + (j - 1)];
                dp[i * (n + 1) + j] = a > b ? a : b;
            }
        }
    }
    int ans = dp[m * (n + 1) + n];
    free(dp);
    return ans;
}
