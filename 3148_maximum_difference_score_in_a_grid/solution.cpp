// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxScore(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = 1 << 30;
        std::vector<std::vector<int>> f(m, std::vector<int>(n));
        int ans = -inf;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                int mi = inf;
                if (i > 0) mi = std::min(mi, f[i - 1][j]);
                if (j > 0) mi = std::min(mi, f[i][j - 1]);
                ans = std::max(ans, x - mi);
                f[i][j] = std::min(x, mi);
            }
        }
        return ans;
    }
};
