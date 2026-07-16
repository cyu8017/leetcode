// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

#include <string.h>

int longestPalindromeSubseq(char* s) {
    const int length = (int)strlen(s);
    int dp[1001][1001];
    for (int index = length - 1; index >= 0; index--) {
        dp[index][index] = 1;
        for (int end = index + 1; end < length; end++) {
            if (s[index] == s[end]) {
                dp[index][end] = dp[index + 1][end - 1] + 2;
            } else {
                int skipStart = dp[index + 1][end];
                int skipEnd = dp[index][end - 1];
                dp[index][end] = skipStart > skipEnd ? skipStart : skipEnd;
            }
        }
    }
    return dp[0][length - 1];
}
