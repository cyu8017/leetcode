// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int longestPalindromeSubseq(std::string s) {
        const int length = static_cast<int>(s.size());
        std::vector<std::vector<int>> dp(length, std::vector<int>(length, 0));
        for (int index = length - 1; index >= 0; --index) {
            dp[index][index] = 1;
            for (int end = index + 1; end < length; ++end) {
                if (s[index] == s[end]) {
                    dp[index][end] = dp[index + 1][end - 1] + 2;
                } else {
                    dp[index][end] = std::max(dp[index + 1][end], dp[index][end - 1]);
                }
            }
        }
        return dp[0][length - 1];
    }
};
