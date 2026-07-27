// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestStrChain(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end(),
                  [](const std::string& a, const std::string& b) { return a.size() < b.size(); });
        std::unordered_map<std::string, int> dp;
        int ans = 1;
        for (const auto& w : words) {
            dp[w] = 1;
            for (int i = 0; i < static_cast<int>(w.size()); ++i) {
                std::string prev = w.substr(0, i) + w.substr(i + 1);
                auto it = dp.find(prev);
                if (it != dp.end()) dp[w] = std::max(dp[w], it->second + 1);
            }
            ans = std::max(ans, dp[w]);
        }
        return ans;
    }
};

