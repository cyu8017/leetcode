// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int findMaxForm(std::vector<std::string>& strs, int m, int n) {
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (const std::string& string : strs) {
            const int zeros = static_cast<int>(
                std::count(string.begin(), string.end(), '0'));
            const int ones = static_cast<int>(string.size()) - zeros;
            for (int zero = m; zero >= zeros; --zero) {
                for (int one = n; one >= ones; --one) {
                    dp[zero][one] = std::max(
                        dp[zero][one], dp[zero - zeros][one - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
};
