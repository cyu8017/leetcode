// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    int minCost(std::string source, std::string target, std::vector<std::vector<std::string>>& rules,
                std::vector<int>& costs) {
        int n = (int)source.size();
        if ((int)target.size() != n) return -1;
        std::vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INT_MAX) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int j = 0; j < (int)rules.size(); j++) {
                const std::string& p = rules[j][0];
                const std::string& r = rules[j][1];
                int plen = (int)p.size();
                if (i + plen > n) continue;
                int c = costs[j];
                bool ok = true;
                for (int k = 0; k < plen; k++) {
                    if (r[k] != target[i + k]) {
                        ok = false;
                        break;
                    }
                    if (p[k] == '*') ++c;
                    else if (p[k] != source[i + k]) {
                        ok = false;
                        break;
                    }
                }
                if (ok && dp[i] <= INT_MAX - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        return dp[n] == INT_MAX ? -1 : dp[n];
    }
};
