// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

#include <vector>
#include <map>
#include <array>

class Solution {
public:
    std::vector<int> treeQueries(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<std::pair<int, int>>> g(n + 1);
        std::map<std::array<int, 2>, int> weight;
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
            int a = std::min(u, v), b = std::max(u, v);
            weight[{a, b}] = w;
        }
        std::vector<int> inT(n + 1), outT(n + 1), dist(n + 1), parent(n + 1);
        int time = 0;
        auto dfs = [&](auto&& self, int u, int p) -> void {
            inT[u] = time++;
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                parent[to] = u;
                dist[to] = dist[u] + w;
                self(self, to, u);
            }
            outT[u] = time - 1;
        };
        dfs(dfs, 1, 0);
        std::vector<int> bit(n + 2);
        auto add = [&](int i, int v) {
            for (; i <= n; i += i & -i) bit[i] += v;
        };
        auto rangeAdd = [&](int l, int r, int v) {
            add(l + 1, v);
            add(r + 2, -v);
        };
        auto point = [&](int i) {
            int s = 0;
            for (i++; i > 0; i -= i & -i) s += bit[i];
            return s;
        };
        for (int i = 1; i <= n; i++) rangeAdd(inT[i], inT[i], dist[i]);
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], nw = q[3];
                int a = std::min(u, v), b = std::max(u, v);
                int ow = weight[{a, b}];
                int delta = nw - ow;
                weight[{a, b}] = nw;
                int child = (parent[u] == v) ? u : v;
                rangeAdd(inT[child], outT[child], delta);
            } else {
                ans.push_back(point(inT[q[1]]));
            }
        }
        return ans;
    }
};
