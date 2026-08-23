// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

#include <vector>

class Solution {
public:
    bool checkValidGrid(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        if (grid[0][0] != 0) return false;
        std::vector<std::pair<int, int>> pos(n * n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                pos[grid[i][j]] = {i, j};
        int dirs[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};
        for (int v = 0; v + 1 < n * n; ++v) {
            int r = pos[v].first, c = pos[v].second;
            bool ok = false;
            for (auto& d : dirs) {
                if (r + d[0] == pos[v + 1].first && c + d[1] == pos[v + 1].second) {
                    ok = true;
                    break;
                }
            }
            if (!ok) return false;
        }
        return true;
    }
};
