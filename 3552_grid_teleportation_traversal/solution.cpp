// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

#include <string>
#include <vector>
#include <deque>
#include <unordered_map>
#include <cctype>

class Solution {
public:
    int minMoves(std::vector<std::string>& matrix) {
        int m = (int)matrix.size(), n = (int)matrix[0].size();
        std::unordered_map<char, std::vector<std::pair<int, int>>> g;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (std::isalpha(matrix[i][j])) g[matrix[i][j]].push_back({i, j});
        int dirs[5] = {-1, 0, 1, 0, -1};
        const int INF = 1 << 30;
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, INF));
        dist[0][0] = 0;
        std::deque<std::pair<int, int>> q;
        q.push_back({0, 0});
        while (!q.empty()) {
            auto [i, j] = q.front(); q.pop_front();
            int d = dist[i][j];
            if (i == m - 1 && j == n - 1) return d;
            char c = matrix[i][j];
            if (g.count(c)) {
                for (auto& [x, y] : g[c]) {
                    if (d < dist[x][y]) {
                        dist[x][y] = d;
                        q.push_front({x, y});
                    }
                }
                g.erase(c);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx], y = j + dirs[idx + 1];
                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != '#' && d + 1 < dist[x][y]) {
                    dist[x][y] = d + 1;
                    q.push_back({x, y});
                }
            }
        }
        return -1;
    }
};
