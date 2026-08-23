// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

#include <vector>
#include <queue>
#include <climits>
#include <unordered_set>

class Solution {
public:
    int minimumDistance(int n, std::vector<std::vector<int>>& edges, int s, std::vector<int>& marked) {
        std::vector<std::vector<std::pair<int,int>>> g(n);
        for (auto& e : edges) g[e[0]].push_back({e[1], e[2]});
        std::unordered_set<int> mark(marked.begin(), marked.end());
        std::vector<int> dist(n, INT_MAX / 4);
        dist[s] = 0;
        using P = std::pair<int,int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (mark.count(u)) return d;
            if (d > dist[u]) continue;
            for (auto [v, w] : g[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return -1;
    }
};
