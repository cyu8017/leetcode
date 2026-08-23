// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<long long> minCost(int n, std::vector<std::vector<int>>& roads, std::vector<int>& appleCost, int k) {
        std::vector<std::vector<std::pair<int, int>>> g(n + 1);
        for (auto& r : roads) {
            g[r[0]].push_back({r[1], r[2]});
            g[r[1]].push_back({r[0], r[2]});
        }
        std::vector<long long> ans(n);
        const long long INF = 1LL << 60;
        for (int start = 1; start <= n; start++) {
            std::vector<long long> dist(n + 1, INF);
            dist[start] = 0;
            using P = std::pair<long long, int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, start});
            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if (d != dist[u]) continue;
                for (auto [v, w] : g[u]) {
                    long long nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.push({nd, v});
                    }
                }
            }
            long long best = INF;
            for (int city = 1; city <= n; city++) {
                long long cost = dist[city] * (k + 1) + appleCost[city - 1];
                if (cost < best) best = cost;
            }
            ans[start - 1] = best;
        }
        return ans;
    }
};
