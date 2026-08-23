// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

#include <algorithm>
#include <vector>

class Solution {
public:
    int getMaximumGold(std::vector<std::vector<int>>& grid) {
        const int rows = static_cast<int>(grid.size());
        const int cols = static_cast<int>(grid[0].size());
        auto dfs = [&](auto&& self, int r, int c) -> int {
            int gold = grid[r][c];
            grid[r][c] = 0;
            int best = 0;
            static const int dr[] = {1, -1, 0, 0};
            static const int dc[] = {0, 0, 1, -1};
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc]) {
                    best = std::max(best, self(self, nr, nc));
                }
            }
            grid[r][c] = gold;
            return gold + best;
        };
        int answer = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c]) {
                    answer = std::max(answer, dfs(dfs, r, c));
                }
            }
        }
        return answer;
    }
};
