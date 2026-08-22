// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int maxPalindromes(char* s, int k) {
    int n = (int)strlen(s);
    bool** isPal = (bool**)malloc((size_t)n * sizeof(bool*));
    for (int i = 0; i < n; i++) {
        isPal[i] = (bool*)calloc((size_t)n, sizeof(bool));
        isPal[i][i] = true;
    }
    for (int i = 0; i + 1 < n; i++) isPal[i][i + 1] = s[i] == s[i + 1];
    for (int length = 3; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            isPal[i][j] = s[i] == s[j] && isPal[i + 1][j - 1];
        }
    }
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        dp[i] = dp[i + 1];
        for (int j = i + k - 1; j < n; j++) {
            if (isPal[i][j] && 1 + dp[j + 1] > dp[i]) dp[i] = 1 + dp[j + 1];
        }
    }
    int ans = dp[0];
    for (int i = 0; i < n; i++) free(isPal[i]);
    free(isPal); free(dp);
    return ans;
}
