// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

#include <stdlib.h>
#include <limits.h>

int minLargest(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size, m = nums2Size;
    const int INF = INT_MAX / 4;
    int** dp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)malloc((size_t)(m + 1) * sizeof(int));
        for (int j = 0; j <= m; j++) dp[i][j] = INF;
    }
    dp[0][0] = 0;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (dp[i][j] == INF) continue;
            int prev = dp[i][j];
            if (i < n) {
                int need = prev + 1;
                if (nums1[i] == 0) { if (need % 2 != 0) need++; }
                else { if (need % 2 == 0) need++; }
                if (need < dp[i + 1][j]) dp[i + 1][j] = need;
            }
            if (j < m) {
                int need = prev + 1;
                if (nums2[j] == 0) { if (need % 2 != 0) need++; }
                else { if (need % 2 == 0) need++; }
                if (need < dp[i][j + 1]) dp[i][j + 1] = need;
            }
        }
    }
    int ans = dp[n][m];
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp);
    return ans;
}
