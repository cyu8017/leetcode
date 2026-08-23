// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

#include <vector>
#include <queue>
#include <climits>
#include <tuple>

class Solution {
public:
    int shortestPathWithHops(int n, std::vector<std::vector<int>>& edges, int s, int d, int k) {
        std::vector<std::vector<std::pair<int,int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        std::vector<std::vector<int>> dist(n, std::vector<int>(k + 1, INT_MAX / 4));
        dist[s][0] = 0;
        using T = std::tuple<int,int,int>; // dist, node, hops
        std::priority_queue<T, std::vector<T>, std::greater<T>> pq;
        pq.push({0, s, 0});
        while (!pq.empty()) {
            auto [cd, u, hops] = pq.top(); pq.pop();
            if (u == d) return cd;
            if (cd > dist[u][hops]) continue;
            for (auto [to, w] : g[u]) {
                if (cd + w < dist[to][hops]) {
                    dist[to][hops] = cd + w;
                    pq.push({dist[to][hops], to, hops});
                }
                if (hops < k && cd < dist[to][hops + 1]) {
                    dist[to][hops + 1] = cd;
                    pq.push({cd, to, hops + 1});
                }
            }
        }
        return -1;
    }
};
