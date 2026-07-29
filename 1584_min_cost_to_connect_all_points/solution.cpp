// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

#include <algorithm>
#include <cmath>
#include <limits>
#include <vector>

class Solution {
public:
    int minCostConnectPoints(std::vector<std::vector<int>>& points) {
        const int n = static_cast<int>(points.size());
        std::vector<bool> used(n, false);
        std::vector<int> dist(n, std::numeric_limits<int>::max());
        dist[0] = 0;
        int answer = 0;
        for (int step = 0; step < n; ++step) {
            int u = -1;
            for (int i = 0; i < n; ++i) {
                if (!used[i] && (u == -1 || dist[i] < dist[u])) {
                    u = i;
                }
            }
            used[u] = true;
            answer += dist[u];
            for (int v = 0; v < n; ++v) {
                if (!used[v]) {
                    const int d = std::abs(points[u][0] - points[v][0]) +
                                  std::abs(points[u][1] - points[v][1]);
                    dist[v] = std::min(dist[v], d);
                }
            }
        }
        return answer;
    }
};
