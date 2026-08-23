// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

#include <string>
#include <vector>

class Solution {
public:
    int maxPalindromes(std::string s, int k) {
        int n = (int)s.size();
        std::vector<std::vector<bool>> isPal(n, std::vector<bool>(n, false));
        for (int i = 0; i < n; i++) isPal[i][i] = true;
        for (int i = 0; i + 1 < n; i++) isPal[i][i + 1] = s[i] == s[i + 1];
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                isPal[i][j] = s[i] == s[j] && isPal[i + 1][j - 1];
            }
        }
        std::vector<int> dp(n + 1);
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = dp[i + 1];
            for (int j = i + k - 1; j < n; j++) {
                if (isPal[i][j] && 1 + dp[j + 1] > dp[i]) dp[i] = 1 + dp[j + 1];
            }
        }
        return dp[0];
    }
};
