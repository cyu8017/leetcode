// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minimumMoves(std::vector<std::vector<int>>& grid) {
        std::vector<std::pair<int, int>> extras, zeros;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) zeros.push_back({i, j});
                else if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) extras.push_back({i, j});
                }
            }
        }
        if (zeros.empty()) return 0;
        int best = 1 << 30;
        auto dfs = [&](auto&& self, int i, int cost) -> void {
            if (cost >= best) return;
            if (i == (int)zeros.size()) { best = cost; return; }
            for (int j = 0; j < (int)extras.size(); j++) {
                if (extras[j].first < 0) continue;
                auto e = extras[j];
                extras[j].first = -1;
                int d = std::abs(e.first - zeros[i].first) + std::abs(e.second - zeros[i].second);
                self(self, i + 1, cost + d);
                extras[j] = e;
            }
        };
        dfs(dfs, 0, 0);
        return best;
    }
};
