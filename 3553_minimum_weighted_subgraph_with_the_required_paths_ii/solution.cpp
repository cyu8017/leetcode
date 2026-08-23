// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minimumWeight(std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        const int LOG = 17;
        std::vector<std::vector<int>> parent(LOG, std::vector<int>(n, -1));
        std::vector<int> depth(n), dist(n);
        auto dfs = [&](auto&& self, int u, int p) -> void {
            parent[0][u] = p;
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                depth[to] = depth[u] + 1;
                dist[to] = dist[u] + w;
                self(self, to, u);
            }
        };
        dfs(dfs, 0, -1);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (parent[k - 1][v] != -1)
                    parent[k][v] = parent[k - 1][parent[k - 1][v]];
        auto lca = [&](int u, int v) {
            if (depth[u] < depth[v]) std::swap(u, v);
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v])
                    u = parent[k][u];
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            return parent[0][u];
        };
        auto path = [&](int u, int v) {
            int a = lca(u, v);
            return dist[u] + dist[v] - 2 * dist[a];
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1], c = queries[i][2];
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) / 2;
        }
        return ans;
    }
};
