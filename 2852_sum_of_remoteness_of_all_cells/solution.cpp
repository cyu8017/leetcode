// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

#include <queue>
#include <vector>

class Solution {
public:
    long long sumRemoteness(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<char>> seen(m, std::vector<char>(n, 0));
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        long long total = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] != -1) total += grid[i][j];
        long long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1 || seen[i][j]) continue;
                std::queue<std::pair<int, int>> q;
                q.push({i, j});
                seen[i][j] = 1;
                long long sum = 0;
                int cnt = 0;
                while (!q.empty()) {
                    auto [x, y] = q.front(); q.pop();
                    sum += grid[x][y];
                    cnt++;
                    for (auto& d : dirs) {
                        int ni = x + d[0], nj = y + d[1];
                        if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1) {
                            seen[ni][nj] = 1;
                            q.push({ni, nj});
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        return ans;
    }
};
