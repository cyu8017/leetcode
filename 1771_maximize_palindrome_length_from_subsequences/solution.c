// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

#include <stdlib.h>
#include <string.h>

int longestPalindrome(char* word1, char* word2) {
    int n1 = (int)strlen(word1);
    int n2 = (int)strlen(word2);
    int n = n1 + n2;
    char* s = (char*)malloc((size_t)(n + 1));
    memcpy(s, word1, (size_t)n1);
    memcpy(s + n1, word2, (size_t)(n2 + 1));

    int** dp = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dp[i] = (int*)calloc((size_t)n, sizeof(int));
    }

    int ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        dp[i][i] = 1;
        for (int j = i + 1; j < n; j++) {
            if (s[i] == s[j]) {
                dp[i][j] = (j == i + 1) ? 2 : dp[i + 1][j - 1] + 2;
                if (i < n1 && n1 <= j && dp[i][j] > ans) {
                    ans = dp[i][j];
                }
            } else {
                dp[i][j] = dp[i + 1][j] > dp[i][j - 1] ? dp[i + 1][j] : dp[i][j - 1];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        free(dp[i]);
    }
    free(dp);
    free(s);
    return ans;
}
