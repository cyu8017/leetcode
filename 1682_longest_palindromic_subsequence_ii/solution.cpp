// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestPalindromeSubseq(std::string s) {
        int n = static_cast<int>(s.size());
        std::vector<std::vector<std::vector<int>>> dp(
            n, std::vector<std::vector<int>>(n, std::vector<int>(26, 0)));
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                for (int c = 0; c < 26; ++c) {
                    dp[i][j][c] = std::max(dp[i + 1][j][c], dp[i][j - 1][c]);
                }
                if (s[i] == s[j]) {
                    int c = s[i] - 'a';
                    int inner = 0;
                    if (length > 2) {
                        for (int x = 0; x < 26; ++x) {
                            if (x != c) {
                                inner = std::max(inner, dp[i + 1][j - 1][x]);
                            }
                        }
                    }
                    dp[i][j][c] = std::max(dp[i][j][c], inner + 2);
                }
            }
        }
        return *std::max_element(dp[0][n - 1].begin(), dp[0][n - 1].end());
    }
};
