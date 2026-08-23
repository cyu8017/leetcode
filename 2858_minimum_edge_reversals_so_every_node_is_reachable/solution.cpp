// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> minEdgeReversals(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back({v, 0});
            g[v].push_back({u, 1});
        }
        std::vector<int> ans(n);
        std::function<void(int, int)> dfs1 = [&](int u, int p) {
            for (auto [v, ww] : g[u]) {
                if (v == p) continue;
                ans[0] += ww;
                dfs1(v, u);
            }
        };
        dfs1(0, -1);
        std::function<void(int, int)> dfs2 = [&](int u, int p) {
            for (auto [v, ww] : g[u]) {
                if (v == p) continue;
                if (ww == 0) ans[v] = ans[u] + 1;
                else ans[v] = ans[u] - 1;
                dfs2(v, u);
            }
        };
        dfs2(0, -1);
        return ans;
    }
};
