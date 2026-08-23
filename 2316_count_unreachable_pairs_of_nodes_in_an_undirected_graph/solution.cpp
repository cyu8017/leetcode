// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

#include <vector>
#include <functional>

class Solution {
public:
    long long countPairs(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<char> vis(n);
        std::function<int(int)> dfs = [&](int u) {
            vis[u] = 1;
            int size = 1;
            for (int v : g[u]) if (!vis[v]) size += dfs(v);
            return size;
        };
        long long ans = 0, seen = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                long long sz = dfs(i);
                ans += sz * seen;
                seen += sz;
            }
        }
        return ans;
    }
};
