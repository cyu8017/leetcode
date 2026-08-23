// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    int palindromePartition(std::string s, int k) {
        const int n = static_cast<int>(s.size());
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 0));
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s[i] != s[j]);
            }
        }
        const int inf = n + 1;
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, inf));
        dp[0][0] = 0;
        for (int parts = 1; parts <= k; ++parts) {
            for (int end = parts; end <= n; ++end) {
                for (int start = parts - 1; start < end; ++start) {
                    dp[parts][end] = std::min(dp[parts][end], dp[parts - 1][start] + cost[start][end - 1]);
                }
            }
        }
        return dp[k][n];
    }
};
