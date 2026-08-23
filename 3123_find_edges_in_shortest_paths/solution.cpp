// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

#include <vector>
#include <queue>
#include <utility>
#include <array>

class Solution {
public:
    std::vector<bool> findAnswer(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::array<int, 3>>> g(n);
        for (int i = 0; i < (int)edges.size(); i++) {
            int a = edges[i][0], b = edges[i][1], w = edges[i][2];
            g[a].push_back({b, w, i});
            g[b].push_back({a, w, i});
        }
        const int inf = 1 << 30;
        std::vector<int> dist(n, inf);
        dist[0] = 0;
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [da, a] = pq.top(); pq.pop();
            if (da > dist[a]) continue;
            for (auto& e : g[a]) {
                int b = e[0], w = e[1];
                if (dist[b] > dist[a] + w) {
                    dist[b] = dist[a] + w;
                    pq.push({dist[b], b});
                }
            }
        }
        std::vector<bool> ans(edges.size(), false);
        if (dist[n - 1] == inf) return ans;
        std::queue<int> q;
        q.push(n - 1);
        while (!q.empty()) {
            int a = q.front(); q.pop();
            for (auto& e : g[a]) {
                int b = e[0], w = e[1], i = e[2];
                if (dist[a] == dist[b] + w) {
                    ans[i] = true;
                    q.push(b);
                }
            }
        }
        return ans;
    }
};
