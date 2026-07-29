// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int strangePrinter(std::string s) {
        const int n = static_cast<int>(s.size());
        if (n == 0) {
            return 0;
        }
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int i = n - 1; i >= 0; --i) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; ++j) {
                dp[i][j] = dp[i + 1][j] + 1;
                for (int k = i + 1; k <= j; ++k) {
                    if (s[k] == s[i]) {
                        dp[i][j] = std::min(
                            dp[i][j],
                            dp[i][k - 1] + (k + 1 <= j ? dp[k + 1][j] : 0));
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
};
