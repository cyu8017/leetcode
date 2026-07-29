// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumMoves(std::vector<int>& arr) {
        const int n = static_cast<int>(arr.size());
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                dp[i][j] = 1 + dp[i + 1][j];
                if (arr[i] == arr[i + 1]) {
                    dp[i][j] = std::min(dp[i][j], 1 + (i + 2 <= j ? dp[i + 2][j] : 0));
                }
                for (int k = i + 2; k <= j; ++k) {
                    if (arr[i] == arr[k]) {
                        dp[i][j] = std::min(dp[i][j], dp[i + 1][k - 1] + (k < j ? dp[k + 1][j] : 0));
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
};
