// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> specialGrid(int n) {
        int m = 1 << n;
        std::vector<std::vector<int>> ans(m, std::vector<int>(m));
        int val = 0;
        auto dfs = [&](auto&& self, int x, int y, int k) -> void {
            if (k == 1) { ans[x][y] = val++; return; }
            int h = k / 2;
            self(self, x, y, h);
            self(self, x + h, y, h);
            self(self, x + h, y - h, h);
            self(self, x, y - h, h);
        };
        dfs(dfs, 0, m - 1, m);
        return ans;
    }
};
