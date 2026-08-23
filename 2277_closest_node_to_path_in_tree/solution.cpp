// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    std::vector<int> closestNode(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& query) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        const int LOG = 17;
        std::vector<std::vector<int>> up(LOG, std::vector<int>(n));
        std::vector<int> depth(n);
        std::function<void(int,int)> dfs = [&](int u, int p) {
            up[0][u] = p;
            for (int v : g[u]) if (v != p) { depth[v] = depth[u] + 1; dfs(v, u); }
        };
        dfs(0, 0);
        for (int k = 1; k < LOG; ++k)
            for (int v = 0; v < n; ++v) up[k][v] = up[k - 1][up[k - 1][v]];
        auto lift = [&](int v, int d) {
            for (int k = 0; k < LOG; ++k) if ((d >> k) & 1) v = up[k][v];
            return v;
        };
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) std::swap(a, b);
            a = lift(a, depth[a] - depth[b]);
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; --k)
                if (up[k][a] != up[k][b]) { a = up[k][a]; b = up[k][b]; }
            return up[0][a];
        };
        auto dist = [&](int a, int b) {
            int c = lca(a, b);
            return depth[a] + depth[b] - 2 * depth[c];
        };
        std::vector<int> ans(query.size());
        for (size_t i = 0; i < query.size(); ++i) {
            int a = query[i][0], b = query[i][1], x = query[i][2];
            int cands[3] = {lca(a, b), lca(a, x), lca(b, x)};
            int best = cands[0], bestD = dist(cands[0], x);
            for (int t = 1; t < 3; ++t) {
                int d = dist(cands[t], x);
                if (d < bestD) { bestD = d; best = cands[t]; }
            }
            ans[i] = best;
        }
        return ans;
    }
};
