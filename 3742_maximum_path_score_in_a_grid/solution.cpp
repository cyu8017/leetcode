// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maxPathScore(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = 1 << 30;
        std::vector<std::vector<std::vector<int>>> f(m, std::vector<std::vector<int>>(n, std::vector<int>(k + 1, -1)));
        std::function<int(int, int, int)> dfs = [&](int i, int j, int kk) -> int {
            if (i < 0 || j < 0 || kk < 0) return -inf;
            if (i == 0 && j == 0) return 0;
            if (f[i][j][kk] != -1) return f[i][j][kk];
            int res = grid[i][j];
            int nk = kk;
            if (grid[i][j] != 0) nk--;
            int a = dfs(i - 1, j, nk);
            int b = dfs(i, j - 1, nk);
            res += std::max(a, b);
            return f[i][j][kk] = res;
        };
        int ans = dfs(m - 1, n - 1, k);
        return ans < 0 ? -1 : ans;
    }
};
