// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

#include <functional>
#include <map>
#include <tuple>
#include <vector>

class Solution {
public:
    bool isThereAPath(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        if ((m + n - 1) % 2 != 0) return false;
        int target = (m + n - 1) / 2;
        std::map<std::tuple<int, int, int>, bool> memo;
        std::function<bool(int, int, int)> dfs = [&](int r, int c, int bal) -> bool {
            if (r >= m || c >= n) return false;
            bal += grid[r][c];
            if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false;
            if (r == m - 1 && c == n - 1) return bal == target;
            auto key = std::make_tuple(r, c, bal);
            if (memo.count(key)) return memo[key];
            bool ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal);
            return memo[key] = ok;
        };
        return dfs(0, 0, 0);
    }
};
