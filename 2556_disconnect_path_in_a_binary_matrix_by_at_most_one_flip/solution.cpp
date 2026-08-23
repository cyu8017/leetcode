// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

#include <functional>
#include <vector>

class Solution {
public:
    bool isPossibleToCutPath(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::function<bool(int, int)> dfs = [&](int r, int c) -> bool {
            if (r == m - 1 && c == n - 1) return true;
            if (r >= m || c >= n || grid[r][c] == 0) return false;
            if (!(r == 0 && c == 0)) grid[r][c] = 0;
            return dfs(r + 1, c) || dfs(r, c + 1);
        };
        if (!dfs(0, 0)) return true;
        grid[0][0] = 1;
        return !dfs(0, 0);
    }
};
