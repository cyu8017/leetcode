// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

#include <vector>

class Solution {
public:
    std::vector<int> baseUnitConversions(std::vector<std::vector<int>>& conversions) {
        const int mod = 1000000007;
        int n = (int)conversions.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : conversions) g[e[0]].push_back({e[1], e[2]});
        std::vector<int> ans(n);
        auto dfs = [&](auto&& self, int s, int mul) -> void {
            ans[s] = mul;
            for (auto& [t, w] : g[s]) self(self, t, (int)(1LL * mul * w % mod));
        };
        dfs(dfs, 0, 1);
        return ans;
    }
};
