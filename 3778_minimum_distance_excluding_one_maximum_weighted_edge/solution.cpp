// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

#include <array>
#include <cstdint>
#include <functional>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

class Solution {
public:
    long long minCostExcludingMax(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        const int64_t INF = (int64_t)4e18;
        std::vector<std::array<int64_t, 2>> dist(n, {INF, INF});
        dist[0][0] = 0;
        using State = std::tuple<int64_t, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
        pq.push({0, 0, 0});
        while (!pq.empty()) {
            auto [cur, u, used] = pq.top();
            pq.pop();
            if (cur > dist[u][used]) continue;
            if (u == n - 1 && used == 1) return cur;
            for (auto [v, w] : g[u]) {
                int64_t nxt = cur + w;
                if (nxt < dist[v][used]) {
                    dist[v][used] = nxt;
                    pq.push({nxt, v, used});
                }
                if (used == 0) {
                    nxt = cur;
                    if (nxt < dist[v][1]) {
                        dist[v][1] = nxt;
                        pq.push({nxt, v, 1});
                    }
                }
            }
        }
        return dist[n - 1][1];
    }
};
