// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

#include <cmath>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexicographicallySmallestString(std::string s) {
        int n = (int)s.size();
        std::vector<std::vector<std::string>> dp(n + 1, std::vector<std::string>(n + 1));
        auto isConsec = [](char a, char b) {
            int d = std::abs(a - b);
            return d == 1 || d == 25;
        };
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length;
                std::string minStr = std::string(1, s[i]) + dp[i + 1][j];
                for (int k = i + 1; k < j; k++) {
                    if (isConsec(s[i], s[k]) && dp[i + 1][k].empty()) {
                        const std::string& cand = dp[k + 1][j];
                        if (cand < minStr) minStr = cand;
                    }
                }
                dp[i][j] = minStr;
            }
        }
        return dp[0][n];
    }
};
