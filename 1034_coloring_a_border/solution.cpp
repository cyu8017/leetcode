// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> colorBorder(std::vector<std::vector<int>>& grid, int row, int col,
                                              int color) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        int original = grid[row][col];
        std::vector<std::vector<bool>> seen(m, std::vector<bool>(n, false));
        std::vector<std::pair<int, int>> component;
        std::vector<std::pair<int, int>> stack{{row, col}};
        seen[row][col] = true;
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.empty()) {
            auto [r, c] = stack.back();
            stack.pop_back();
            component.push_back({r, c});
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original &&
                    !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    stack.push_back({nr, nc});
                }
            }
        }
        for (auto [r, c] : component) {
            bool border = false;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || !seen[nr][nc]) {
                    border = true;
                    break;
                }
            }
            if (border) grid[r][c] = color;
        }
        return grid;
    }
};

