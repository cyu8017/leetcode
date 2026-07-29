#include <set>
#include <utility>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasValidPath(std::vector<std::vector<int>>& grid) {
        static const std::vector<std::pair<int,int>> dirs[7] = {
            {}, {{0,-1},{0,1}}, {{-1,0},{1,0}}, {{0,-1},{1,0}},
            {{0,1},{1,0}}, {{0,-1},{-1,0}}, {{0,1},{-1,0}}
        };
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::set<std::pair<int,int>> seen{{0,0}};
        std::vector<std::pair<int,int>> st{{0,0}};
        while (!st.empty()) {
            auto [r, c] = st.back(); st.pop_back();
            if (r == m - 1 && c == n - 1) return true;
            for (auto [dr, dc] : dirs[grid[r][c]]) {
                int x = r + dr, y = c + dc;
                if (x >= 0 && x < m && y >= 0 && y < n && !seen.count({x, y})) {
                    bool ok = false;
                    for (auto [odr, odc] : dirs[grid[x][y]])
                        if (odr == -dr && odc == -dc) ok = true;
                    if (ok) { seen.insert({x, y}); st.push_back({x, y}); }
                }
            }
        }
        return false;
    }
};
