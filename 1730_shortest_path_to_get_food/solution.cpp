// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

#include <array>
#include <queue>
#include <vector>

class Solution {
public:
    int getFood(std::vector<std::vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        std::queue<std::array<int, 3>> queue;
        std::vector<std::vector<bool>> seen(rows, std::vector<bool>(cols, false));
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '*') {
                    queue.push({r, c, 0});
                    seen[r][c] = true;
                }
            }
        }
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.empty()) {
            auto [r, c, d] = queue.front();
            queue.pop();
            if (grid[r][c] == '#') {
                return d;
            }
            for (const auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] != 'X') {
                    seen[nr][nc] = true;
                    queue.push({nr, nc, d + 1});
                }
            }
        }
        return -1;
    }
};
