// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    bool isValidPalindrome(std::string s, int k) {
        const int n = static_cast<int>(s.size());
        if (n == 0) {
            return true;
        }
        std::vector<int> dp(n, 0);
        for (int i = n - 1; i >= 0; --i) {
            int previous = 0;
            for (int j = i + 1; j < n; ++j) {
                int old = dp[j];
                if (s[i] == s[j]) {
                    dp[j] = previous;
                } else {
                    dp[j] = 1 + std::min(dp[j], dp[j - 1]);
                }
                previous = old;
            }
        }
        return dp[n - 1] <= k;
    }
};
