// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

#include <queue>
#include <vector>

class Solution {
public:
    int shortestPathBinaryMatrix(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        if (grid[0][0] || grid[n - 1][n - 1]) {
            return -1;
        }
        std::queue<std::tuple<int, int, int>> q;
        q.emplace(0, 0, 1);
        grid[0][0] = 1;
        static const int dr[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
        static const int dc[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
        while (!q.empty()) {
            auto [r, c, dist] = q.front();
            q.pop();
            if (r == n - 1 && c == n - 1) {
                return dist;
            }
            for (int k = 0; k < 8; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    q.emplace(nr, nc, dist + 1);
                }
            }
        }
        return -1;
    }
};
