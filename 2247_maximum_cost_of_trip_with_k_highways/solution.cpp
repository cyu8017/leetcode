// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumCost(int n, std::vector<std::vector<int>>& highways, int k) {
        if (k + 1 > n) return -1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& h : highways) {
            g[h[0]].push_back({h[1], h[2]});
            g[h[1]].push_back({h[0], h[2]});
        }
        std::vector<std::vector<int>> dp(1 << n, std::vector<int>(n, -1));
        for (int i = 0; i < n; ++i) dp[1 << i][i] = 0;
        int ans = -1;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int cities = __builtin_popcount(mask);
            for (int u = 0; u < n; ++u) {
                if (dp[mask][u] < 0) continue;
                if (cities - 1 == k) ans = std::max(ans, dp[mask][u]);
                for (auto [v, w] : g[u]) {
                    if (mask & (1 << v)) continue;
                    int nm = mask | (1 << v);
                    dp[nm][v] = std::max(dp[nm][v], dp[mask][u] + w);
                }
            }
        }
        return ans;
    }
};
