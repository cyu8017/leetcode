// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

#include <vector>
#include <queue>
#include <cmath>
#include <climits>

class Solution {
public:
    int minimumCost(std::vector<int>& start, std::vector<int>& target, std::vector<std::vector<int>>& specialRoads) {
        std::vector<std::vector<int>> points = {start, target};
        for (auto& r : specialRoads) {
            points.push_back({r[0], r[1]});
            points.push_back({r[2], r[3]});
        }
        int N = (int)points.size();
        auto distMan = [](std::vector<int>& a, std::vector<int>& b) {
            return std::abs(a[0]-b[0]) + std::abs(a[1]-b[1]);
        };
        std::vector<std::vector<std::pair<int,int>>> g(N);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (i != j) g[i].push_back({j, distMan(points[i], points[j])});
        for (auto& r : specialRoads) {
            int u = -1, v = -1;
            for (int i = 0; i < N; i++) {
                if (points[i][0] == r[0] && points[i][1] == r[1]) u = i;
                if (points[i][0] == r[2] && points[i][1] == r[3]) v = i;
            }
            if (u >= 0 && v >= 0) g[u].push_back({v, r[4]});
        }
        std::vector<int> dist(N, INT_MAX / 4);
        dist[0] = 0;
        using P = std::pair<int,int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [cost, id] = pq.top(); pq.pop();
            if (cost > dist[id]) continue;
            for (auto [to, w] : g[id]) {
                if (cost + w < dist[to]) {
                    dist[to] = cost + w;
                    pq.push({dist[to], to});
                }
            }
        }
        return dist[1];
    }
};
