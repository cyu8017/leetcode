// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

#include <array>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minOperationsQueries(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        const int LOG = 15;
        std::vector<std::vector<int>> up(LOG, std::vector<int>(n));
        std::vector<int> depth(n);
        std::vector<std::array<int, 27>> cnt(n);
        auto dfs = [&](auto&& self, int u, int p) -> void {
            up[0][u] = p;
            for (auto [v, w] : g[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                cnt[v] = cnt[u];
                cnt[v][w]++;
                self(self, v, u);
            }
        };
        dfs(dfs, 0, 0);
        for (int j = 1; j < LOG; j++)
            for (int i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) std::swap(a, b);
            int diff = depth[a] - depth[b];
            for (int j = 0; j < LOG; j++) if (diff & (1 << j)) a = up[j][a];
            if (a == b) return a;
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
            }
            return up[0][a];
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1];
            int c = lca(a, b);
            int total = depth[a] + depth[b] - 2 * depth[c];
            int best = 0;
            for (int w = 1; w <= 26; w++) {
                int f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                best = std::max(best, f);
            }
            ans[i] = total - best;
        }
        return ans;
    }
};
