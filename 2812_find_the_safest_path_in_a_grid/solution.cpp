// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

#include <queue>
#include <vector>

class Solution {
public:
    int maximumSafenessFactor(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        std::vector<std::vector<int>> dist(n, std::vector<int>(n, -1));
        std::queue<std::pair<int, int>> q;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) { dist[i][j] = 0; q.push({i, j}); }
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (auto& d : dirs) {
                int ni = x + d[0], nj = y + d[1];
                if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[x][y] + 1;
                    q.push({ni, nj});
                }
            }
        }
        auto ok = [&](int sf) {
            if (dist[0][0] < sf) return false;
            std::vector<std::vector<char>> seen(n, std::vector<char>(n, 0));
            std::vector<std::pair<int, int>> st{{0, 0}};
            seen[0][0] = 1;
            while (!st.empty()) {
                auto [x, y] = st.back(); st.pop_back();
                if (x == n - 1 && y == n - 1) return true;
                for (auto& d : dirs) {
                    int ni = x + d[0], nj = y + d[1];
                    if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf) {
                        seen[ni][nj] = 1;
                        st.push_back({ni, nj});
                    }
                }
            }
            return false;
        };
        int lo = 0, hi = n * n, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
};
