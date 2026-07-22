// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int numWays(std::vector<std::string>& words, std::string target) {
        const int MOD = 1000000007;
        const int m = static_cast<int>(words[0].size());
        const int n = static_cast<int>(target.size());
        std::vector<long long> dp(n + 1, 0);
        dp[0] = 1;
        for (int j = 0; j < m; ++j) {
            int count[26] = {};
            for (const auto& word : words) {
                ++count[word[j] - 'a'];
            }
            for (int i = std::min(j + 1, n); i >= 1; --i) {
                dp[i] = (dp[i] + dp[i - 1] * count[target[i - 1] - 'a']) % MOD;
            }
        }
        return static_cast<int>(dp[n]);
    }
};
