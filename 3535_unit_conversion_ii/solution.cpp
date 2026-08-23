// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

#include <vector>

class Solution {
    static const int MOD = 1000000007;
    long long qpow(long long x, int n) {
        long long res = 1;
        while (n > 0) {
            if (n & 1) res = res * x % MOD;
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }
public:
    std::vector<int> queryConversions(std::vector<std::vector<int>>& conversions, std::vector<std::vector<int>>& queries) {
        int n = (int)conversions.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : conversions) g[e[0]].push_back({e[1], e[2]});
        std::vector<int> res(n);
        auto dfs = [&](auto&& self, int s, int mul) -> void {
            res[s] = mul;
            for (auto& [t, w] : g[s]) self(self, t, (int)(1LL * mul * w % MOD));
        };
        dfs(dfs, 0, 1);
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++)
            ans[i] = (int)(1LL * res[queries[i][1]] * qpow(res[queries[i][0]], MOD - 2) % MOD);
        return ans;
    }
};
