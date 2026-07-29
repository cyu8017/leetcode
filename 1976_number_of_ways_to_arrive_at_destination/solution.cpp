// LeetCode 1976 - Number of Ways to Arrive at Destination
#include <climits>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int countPaths(int n, std::vector<std::vector<int>>& roads) {
        const int MOD = 1000000007;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& r : roads) {
            g[r[0]].push_back({r[1], r[2]});
            g[r[1]].push_back({r[0], r[2]});
        }
        std::vector<long long> dist(n, LLONG_MAX);
        std::vector<int> ways(n, 0);
        dist[0] = 0;
        ways[0] = 1;
        using Node = std::pair<long long, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            for (auto [v, w] : g[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.push({nd, v});
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return ways[n - 1];
    }
};
