// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

#include <string>
#include <vector>

class Solution {
public:
    int minimumChanges(std::string s, int k) {
        int n = (int)s.size();
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 1 << 20));
        auto semiCost = [&](int l, int r) {
            int length = r - l + 1, best = 1 << 20;
            for (int d = 1; d < length; d++) {
                if (length % d != 0) continue;
                int chg = 0;
                for (int start = 0; start < d; start++) {
                    std::string chars;
                    for (int i = l + start; i <= r; i += d) chars.push_back(s[i]);
                    for (int i = 0, j = (int)chars.size() - 1; i < j; i++, j--)
                        if (chars[i] != chars[j]) chg++;
                }
                if (chg < best) best = chg;
            }
            return best;
        };
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                cost[i][j] = semiCost(i, j);
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 1 << 20));
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++)
            for (int i = 1; i <= n; i++)
                for (int t = 0; t < i - 1; t++) {
                    int cand = dp[p - 1][t] + cost[t][i - 1];
                    if (cand < dp[p][i]) dp[p][i] = cand;
                }
        return dp[k][n];
    }
};
