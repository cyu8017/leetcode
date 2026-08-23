// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

#include <queue>
#include <utility>
#include <vector>

class Solution {
    struct Edge {
        int to, empty, full;
    };

public:
    std::vector<long long> minCostToBuyApples(int n, std::vector<int>& prices, std::vector<std::vector<int>>& roads) {
        std::vector<std::vector<Edge>> g(n);
        for (auto& road : roads) {
            Edge e{road[1], road[2], road[2] * road[3]};
            g[road[0]].push_back(e);
            e.to = road[0];
            g[road[1]].push_back(e);
        }
        const long long inf = 1LL << 62;
        auto dijkstra = [&](int source, bool carrying) {
            std::vector<long long> dist(n, inf);
            dist[source] = 0;
            using P = std::pair<long long, int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, source});
            while (!pq.empty()) {
                auto [d, node] = pq.top();
                pq.pop();
                if (d != dist[node]) continue;
                for (auto& e : g[node]) {
                    int weight = carrying ? e.full : e.empty;
                    long long next = d + weight;
                    if (next < dist[e.to]) {
                        dist[e.to] = next;
                        pq.push({next, e.to});
                    }
                }
            }
            return dist;
        };
        std::vector<long long> answer(n);
        for (int source = 0; source < n; source++) {
            auto emptyDist = dijkstra(source, false);
            auto fullDist = dijkstra(source, true);
            long long best = prices[source];
            for (int shop = 0; shop < n; shop++) {
                if (emptyDist[shop] == inf || fullDist[shop] == inf) continue;
                long long total = emptyDist[shop] + fullDist[shop] + prices[shop];
                if (total < best) best = total;
            }
            answer[source] = best;
        }
        return answer;
    }
};
