// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumCost(std::string target, std::vector<std::string>& words, std::vector<int>& costs) {
        const int64_t inf = (int64_t)1e18;
        int n = (int)target.size();
        std::vector<int64_t> dp(n + 1, inf);
        dp[0] = 0;
        std::unordered_map<std::string, int> best;
        for (int i = 0; i < (int)words.size(); i++) {
            auto it = best.find(words[i]);
            if (it == best.end() || costs[i] < it->second) best[words[i]] = costs[i];
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            for (auto& [w, c] : best) {
                int L = (int)w.size();
                if (i + L <= n && target.compare(i, L, w) == 0 && dp[i] + c < dp[i + L]) {
                    dp[i + L] = dp[i] + c;
                }
            }
        }
        if (dp[n] == inf) return -1;
        return (int)dp[n];
    }
};
