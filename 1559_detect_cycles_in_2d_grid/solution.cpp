// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

#include <vector>

class Solution {
public:
    bool containsCycle(std::vector<std::vector<char>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        std::vector<std::vector<bool>> seen(m, std::vector<bool>(n, false));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (!seen[r][c] && dfs(grid, seen, r, c, -1, -1)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(std::vector<std::vector<char>>& grid, std::vector<std::vector<bool>>& seen,
             int r, int c, int pr, int pc) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        seen[r][c] = true;
        static const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (const auto& d : dirs) {
            const int nr = r + d[0];
            const int nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] != grid[r][c] ||
                (nr == pr && nc == pc)) {
                continue;
            }
            if (seen[nr][nc] || dfs(grid, seen, nr, nc, r, c)) {
                return true;
            }
        }
        return false;
    }
};
