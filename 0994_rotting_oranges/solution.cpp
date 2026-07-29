// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int orangesRotting(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::queue<std::pair<int, int>> q;
        int fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.emplace(i, j);
                else if (grid[i][j] == 1) fresh++;
            }
        }
        int minutes = 0;
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty() && fresh) {
            int sz = (int)q.size();
            for (int s = 0; s < sz; s++) {
                auto [r, c] = q.front();
                q.pop();
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.emplace(nr, nc);
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
};
