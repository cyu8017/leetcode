// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    int minimumSeconds(std::vector<std::vector<std::string>>& land) {
        int m = (int)land.size(), n = (int)land[0].size();
        const int INF = 1 << 30;
        std::vector<std::vector<int>> water(m, std::vector<int>(n, INF));
        std::queue<std::pair<int, int>> wq;
        std::pair<int, int> start{}, dest{};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == "*") { water[i][j] = 0; wq.push({i, j}); }
                else if (land[i][j] == "S") start = {i, j};
                else if (land[i][j] == "D") dest = {i, j};
            }
        }
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!wq.empty()) {
            auto [x, y] = wq.front(); wq.pop();
            for (auto& d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
                if (land[ni][nj] == "X" || land[ni][nj] == "D") continue;
                if (water[ni][nj] > water[x][y] + 1) {
                    water[ni][nj] = water[x][y] + 1;
                    wq.push({ni, nj});
                }
            }
        }
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, -1));
        std::queue<std::pair<int, int>> q;
        q.push(start);
        dist[start.first][start.second] = 0;
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            if (x == dest.first && y == dest.second) return dist[x][y];
            for (auto& d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1) continue;
                if (land[ni][nj] == "X") continue;
                int nd = dist[x][y] + 1;
                if (land[ni][nj] != "D" && nd >= water[ni][nj]) continue;
                dist[ni][nj] = nd;
                q.push({ni, nj});
            }
        }
        return -1;
    }
};
