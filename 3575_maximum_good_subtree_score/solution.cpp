// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int goodSubtreeSum(std::vector<int>& vals, std::vector<int>& par) {
        const int MOD = 1000000007;
        int n = (int)vals.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[par[i]].push_back(i);
        int ans = 0;
        auto digitMask = [](int x) -> std::tuple<int, bool, int> {
            int v = x, mask = 0;
            if (x == 0) return {1, true, 0};
            while (x > 0) {
                int d = x % 10;
                if (mask & (1 << d)) return {0, false, 0};
                mask |= 1 << d;
                x /= 10;
            }
            return {mask, true, v};
        };
        auto dfs = [&](auto&& self, int u) -> std::unordered_map<int, int> {
            std::unordered_map<int, int> dp{{0, 0}};
            auto [mask, ok, v] = digitMask(vals[u]);
            if (ok) dp[mask] = v;
            for (int c : g[u]) {
                auto child = self(self, c);
                std::unordered_map<int, int> ndp;
                for (auto& [m1, s1] : dp) {
                    for (auto& [m2, s2] : child) {
                        if ((m1 & m2) == 0) {
                            int nm = m1 | m2;
                            ndp[nm] = std::max(ndp[nm], s1 + s2);
                        }
                    }
                }
                for (auto& [m, s] : dp) ndp[m] = std::max(ndp[m], s);
                for (auto& [m, s] : child) ndp[m] = std::max(ndp[m], s);
                dp = std::move(ndp);
            }
            int best = 0;
            for (auto& [_, s] : dp) best = std::max(best, s);
            ans = (ans + best) % MOD;
            return dp;
        };
        dfs(dfs, 0);
        return ans;
    }
};
