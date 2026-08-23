// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int assignEdgeWeights(std::vector<std::vector<int>>& edges) {
        const int mod = 1000000007;
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        auto dfs = [&](auto&& self, int i, int fa) -> int {
            int res = 0;
            for (int j : g[i]) {
                if (j != fa) res = std::max(res, self(self, j, i) + 1);
            }
            return res;
        };
        auto pow2 = [&](int exp) {
            long long a = 2, res = 1;
            while (exp > 0) {
                if (exp & 1) res = res * a % mod;
                a = a * a % mod;
                exp >>= 1;
            }
            return (int)res;
        };
        return pow2(dfs(dfs, 1, 0) - 1);
    }
};
