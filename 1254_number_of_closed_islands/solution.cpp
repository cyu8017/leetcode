// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

#include <utility>
#include <vector>

class Solution {
public:
    int closedIsland(std::vector<std::vector<int>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        auto flood = [&](int sr, int sc) {
            std::vector<std::pair<int, int>> stack{{sr, sc}};
            grid[sr][sc] = 1;
            bool closed = true;
            static const int dr[] = {1, -1, 0, 0};
            static const int dc[] = {0, 0, 1, -1};
            while (!stack.empty()) {
                auto [r, c] = stack.back();
                stack.pop_back();
                if (r == 0 || r == m - 1 || c == 0 || c == n - 1) {
                    closed = false;
                }
                for (int i = 0; i < 4; ++i) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        stack.push_back({nr, nc});
                    }
                }
            }
            return closed;
        };
        int answer = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0 && flood(r, c)) {
                    ++answer;
                }
            }
        }
        return answer;
    }
};
