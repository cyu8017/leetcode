// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

#include <cstdlib>
#include <queue>
#include <vector>

class Solution {
public:
    int maxPartitionFactor(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        if (n == 2) return 0;
        auto dist = [&](int i, int j) {
            return std::abs(points[i][0] - points[j][0]) + std::abs(points[i][1] - points[j][1]);
        };
        auto ok = [&](int d) {
            std::vector<std::vector<int>> g(n);
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (dist(i, j) < d) {
                        g[i].push_back(j);
                        g[j].push_back(i);
                    }
                }
            }
            std::vector<int> color(n, -1);
            for (int i = 0; i < n; i++) {
                if (color[i] != -1) continue;
                std::queue<int> q;
                q.push(i);
                color[i] = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : g[u]) {
                        if (color[v] == -1) {
                            color[v] = color[u] ^ 1;
                            q.push(v);
                        } else if (color[v] == color[u]) return false;
                    }
                }
            }
            return true;
        };
        int lo = 0, hi = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                hi = std::max(hi, dist(i, j));
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
