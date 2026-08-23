// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> minimumTime(int n, std::vector<std::vector<int>>& edges, std::vector<int>& disappear) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        const int INF = 1 << 30;
        std::vector<int> dist(n, INF);
        dist[0] = 0;
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [du, u] = pq.top();
            pq.pop();
            if (du > dist[u]) continue;
            for (auto [v, w] : g[u]) {
                if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++)
            ans[i] = dist[i] < disappear[i] ? dist[i] : -1;
        return ans;
    }
};
