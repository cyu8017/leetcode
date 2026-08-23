// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int minExtraChar(std::string s, std::vector<std::string>& dictionary) {
        std::unordered_set<std::string> dict(dictionary.begin(), dictionary.end());
        int n = (int)s.size();
        std::vector<int> dp(n + 1, n);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            dp[i + 1] = std::min(dp[i + 1], dp[i] + 1);
            for (int j = i + 1; j <= n; j++) {
                if (dict.count(s.substr(i, j - i)))
                    dp[j] = std::min(dp[j], dp[i]);
            }
        }
        return dp[n];
    }
};
