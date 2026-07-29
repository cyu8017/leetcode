// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

#include <stdlib.h>
#include <string.h>

int longestCommonSubsequence(char* text1, char* text2) {
    int m = (int)strlen(text1), n = (int)strlen(text2);
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 1; i <= m; i++) {
        int prev = 0;
        for (int j = 1; j <= n; j++) {
            int cur = dp[j];
            if (text1[i - 1] == text2[j - 1]) dp[j] = prev + 1;
            else dp[j] = dp[j] > dp[j - 1] ? dp[j] : dp[j - 1];
            prev = cur;
        }
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
