// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

#include <vector>
#include <functional>

class Solution {
public:
    std::vector<std::vector<int>> tourOfKnight(int m, int n, int r, int c) {
        std::vector<std::vector<int>> ans(m, std::vector<int>(n, -1));
        int dirs[8][2] = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
        std::function<bool(int,int,int)> dfs = [&](int x, int y, int step) -> bool {
            ans[x][y] = step;
            if (step == m * n - 1) return true;
            for (auto& d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1)
                    if (dfs(nx, ny, step + 1)) return true;
            }
            ans[x][y] = -1;
            return false;
        };
        dfs(r, c, 0);
        return ans;
    }
};
