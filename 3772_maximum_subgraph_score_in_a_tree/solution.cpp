// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

#include <vector>

class Solution {
public:
    std::vector<int> maxSubgraphScore(int n, std::vector<std::vector<int>>& edges, std::vector<int>& good) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        std::vector<int> down(n);
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            down[u] = 2 * good[u] - 1;
            for (int v : g[u]) {
                if (parent[v] == u && down[v] > 0) down[u] += down[v];
            }
        }
        std::vector<int> ans = down;
        for (int u : order) {
            for (int v : g[u]) {
                if (parent[v] == u) {
                    int outside = ans[u];
                    if (down[v] > 0) outside -= down[v];
                    ans[v] = down[v];
                    if (outside > 0) ans[v] += outside;
                }
            }
        }
        return ans;
    }
};
