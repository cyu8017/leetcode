// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int minTime(int n, std::vector<std::vector<int>>& edges) {
        struct Edge { int to, start, end; };
        std::vector<std::vector<Edge>> g(n);
        for (auto& e : edges) g[e[0]].push_back({e[1], e[2], e[3]});
        const long long inf = (long long)1e18;
        std::vector<long long> dist(n, inf);
        dist[0] = 0;
        using P = std::pair<long long, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [t, u] = pq.top();
            pq.pop();
            if (t != dist[u]) continue;
            if (u == n - 1) return (int)t;
            for (auto& e : g[u]) {
                long long nt = t;
                if (nt > e.end) continue;
                if (nt < e.start) nt = e.start;
                nt += 1;
                if (nt < dist[e.to]) {
                    dist[e.to] = nt;
                    pq.push({nt, e.to});
                }
            }
        }
        return dist[n - 1] == inf ? -1 : (int)dist[n - 1];
    }
};
