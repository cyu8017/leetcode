// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

#include <cstdint>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<long long> minTimeMaxPower(int n, std::vector<std::vector<int>>& edges, int power,
                                           std::vector<int>& cost, int source, int target) {
        const long long INF = 1LL << 62;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
        }

        std::vector<std::vector<long long>> dist(n, std::vector<long long>(power + 1, INF));
        // state: {d, -p, u} so smaller d first, then larger remaining power (smaller -p)
        using State = std::tuple<long long, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
        pq.emplace(0, -power, source);
        dist[source][power] = 0;

        while (!pq.empty()) {
            auto [d, negP, u] = pq.top();
            pq.pop();
            int p = -negP;
            if (u == target) {
                return {d, (long long)p};
            }
            if (d > dist[u][p] || p < cost[u]) continue;
            p -= cost[u];
            for (auto [v, t] : g[u]) {
                long long nd = d + t;
                if (nd < dist[v][p]) {
                    dist[v][p] = nd;
                    pq.emplace(nd, -p, v);
                }
            }
        }
        return {-1, -1};
    }
};
