// LeetCode 1928 - Minimum Cost to Reach Destination in Time
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int minCost(int maxTime, std::vector<std::vector<int>>& edges, std::vector<int>& passingFee) {
        int n = (int)passingFee.size();
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back({e[1], e[2]});
            graph[e[1]].push_back({e[0], e[2]});
        }
        std::vector<int> minTime(n, maxTime + 1);
        using Node = std::tuple<int, int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<>> pq;
        pq.emplace(passingFee[0], 0, 0);
        while (!pq.empty()) {
            auto [cost, time, u] = pq.top();
            pq.pop();
            if (time >= minTime[u]) continue;
            minTime[u] = time;
            if (u == n - 1) return cost;
            for (auto [v, dt] : graph[u]) {
                int nt = time + dt;
                if (nt <= maxTime && nt < minTime[v]) {
                    pq.emplace(cost + passingFee[v], nt, v);
                }
            }
        }
        return -1;
    }
};
