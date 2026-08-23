// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> assignEdgeWeights(std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        const int MOD = 1000000007;
        const int LOG = 17;
        int n = (int)edges.size() + 1;
        std::vector<int> depth(n + 1);
        std::vector<std::vector<int>> graph(n + 1);
        std::vector<std::vector<int>> parent(LOG, std::vector<int>(n + 1, -1));
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        auto dfs = [&](auto&& self, int u, int p) -> void {
            parent[0][u] = p;
            for (int v : graph[u]) {
                if (v != p) {
                    depth[v] = depth[u] + 1;
                    self(self, v, u);
                }
            }
        };
        dfs(dfs, 1, -1);
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
            }
        }
        auto lca = [&](int u, int v) {
            if (depth[u] < depth[v]) std::swap(u, v);
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u];
            }
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            }
            return parent[0][u];
        };
        auto modPow = [&](int exp) {
            long long base = 2, res = 1;
            while (exp > 0) {
                if (exp & 1) res = res * base % MOD;
                base = base * base % MOD;
                exp >>= 1;
            }
            return (int)res;
        };
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                ans[i] = 0;
                continue;
            }
            int a = lca(u, v);
            int d = depth[u] + depth[v] - 2 * depth[a];
            ans[i] = modPow(d - 1);
        }
        return ans;
    }
};
