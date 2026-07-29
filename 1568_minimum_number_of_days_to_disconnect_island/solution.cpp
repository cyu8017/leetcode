// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

#include <stack>
#include <utility>
#include <vector>

class Solution {
public:
    int minDays(std::vector<std::vector<int>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());

        auto islands = [&]() -> int {
            std::vector<std::vector<bool>> seen(m, std::vector<bool>(n, false));
            int count = 0;
            for (int r = 0; r < m; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (grid[r][c] && !seen[r][c]) {
                        ++count;
                        std::stack<std::pair<int, int>> stack;
                        stack.push({r, c});
                        seen[r][c] = true;
                        while (!stack.empty()) {
                            auto [x, y] = stack.top();
                            stack.pop();
                            static const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
                            for (const auto& d : dirs) {
                                const int nx = x + d[0];
                                const int ny = y + d[1];
                                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] &&
                                    !seen[nx][ny]) {
                                    seen[nx][ny] = true;
                                    stack.push({nx, ny});
                                }
                            }
                        }
                    }
                }
            }
            return count;
        };

        if (islands() != 1) {
            return 0;
        }
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c]) {
                    grid[r][c] = 0;
                    if (islands() != 1) {
                        grid[r][c] = 1;
                        return 1;
                    }
                    grid[r][c] = 1;
                }
            }
        }
        return 2;
    }
};
