// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

#include <vector>
#include <queue>
#include <climits>

class Solution {
public:
    std::vector<std::vector<int>> modifiedGraphEdges(int n, std::vector<std::vector<int>>& edges, int source, int destination, int target) {
        const int INF = 2000000000;
        auto dijkstra = [&](bool ignoreNeg) {
            std::vector<int> dist(n, INF);
            dist[source] = 0;
            using P = std::pair<int,int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, source});
            while (!pq.empty()) {
                auto [d, u] = pq.top(); pq.pop();
                if (d != dist[u]) continue;
                for (int i = 0; i < (int)edges.size(); i++) {
                    int a = edges[i][0], b = edges[i][1], w = edges[i][2];
                    if (a != u && b != u) continue;
                    int to = a == u ? b : a;
                    if (w == -1) {
                        if (ignoreNeg) continue;
                        w = 1;
                    }
                    if (d + w < dist[to]) {
                        dist[to] = d + w;
                        pq.push({dist[to], to});
                    }
                }
            }
            return dist;
        };
        auto d = dijkstra(true);
        if (d[destination] < target) return {};
        bool matched = d[destination] == target;
        for (int i = 0; i < (int)edges.size(); i++) {
            if (edges[i][2] != -1) continue;
            if (matched) { edges[i][2] = INF; continue; }
            edges[i][2] = 1;
            d = dijkstra(false);
            if (d[destination] <= target) {
                edges[i][2] += target - d[destination];
                matched = true;
            }
        }
        d = dijkstra(false);
        if (d[destination] != target) return {};
        return edges;
    }
};
