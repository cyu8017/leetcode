// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int deleteString(std::string s) {
        int n = (int)s.size();
        std::vector<std::vector<int>> lcp(n + 1, std::vector<int>(n + 1));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (s[i] == s[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
            }
        }
        std::vector<int> dp(n);
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = 1;
            for (int len = 1; i + 2 * len <= n; len++) {
                if (lcp[i][i + len] >= len) {
                    dp[i] = std::max(dp[i], 1 + dp[i + len]);
                }
            }
        }
        return dp[0];
    }
};
