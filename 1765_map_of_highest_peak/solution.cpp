// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> highestPeak(std::vector<std::vector<int>>& isWater) {
        int m = (int)isWater.size();
        int n = (int)isWater[0].size();
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, -1));
        std::queue<std::pair<int, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j]) {
                    dist[i][j] = 0;
                    q.push({i, j});
                }
            }
        }
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();
            for (const auto& d : dirs) {
                int x = i + d[0];
                int y = j + d[1];
                if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1) {
                    dist[x][y] = dist[i][j] + 1;
                    q.push({x, y});
                }
            }
        }
        return dist;
    }
};
