// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> lastMarkedNodes(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        auto bfs = [&](int start) {
            std::vector<int> dist(n, -1);
            std::queue<int> q;
            q.push(start);
            dist[start] = 0;
            int far = start;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                if (dist[u] > dist[far]) far = u;
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return std::make_pair(far, dist);
        };
        auto [u, _] = bfs(0);
        auto [v, du] = bfs(u);
        auto [__, dv] = bfs(v);
        (void)__;
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = du[i] >= dv[i] ? u : v;
        return ans;
    }
};
