// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> colorGrid(int n, int m, std::vector<std::vector<int>>& sources) {
        std::vector<std::vector<int>> ans(n, std::vector<int>(m, 0));
        std::vector<std::vector<int>> q = sources;
        int dirs[5] = {-1, 0, 1, 0, -1};
        for (auto& s : q) ans[s[0]][s[1]] = s[2];
        while (!q.empty()) {
            std::map<std::pair<int, int>, int> vis;
            for (auto& curr : q) {
                int r = curr[0], c = curr[1], color = curr[2];
                for (int i = 0; i < 4; i++) {
                    int x = r + dirs[i], y = c + dirs[i + 1];
                    if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                        auto key = std::make_pair(x, y);
                        if (color > vis[key]) vis[key] = color;
                    }
                }
            }
            q.clear();
            for (auto& [pos, color] : vis) {
                ans[pos.first][pos.second] = color;
                q.push_back({pos.first, pos.second, color});
            }
        }
        return ans;
    }
};
