// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

#include <vector>
#include <set>
#include <tuple>
#include <functional>

class Solution {
public:
    bool hasValidPath(std::vector<std::vector<char>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        if ((m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;
        std::set<std::tuple<int,int,int>> vis;
        std::function<bool(int,int,int)> dfs = [&](int r, int c, int bal) -> bool {
            if (r >= m || c >= n) return false;
            bal += (grid[r][c] == '(') ? 1 : -1;
            if (bal < 0) return false;
            if (r == m - 1 && c == n - 1) return bal == 0;
            auto k = std::make_tuple(r, c, bal);
            if (vis.count(k)) return false;
            vis.insert(k);
            return dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
        };
        return dfs(0, 0, 0);
    }
};
