// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

#include <functional>
#include <vector>

class Solution {
public:
    int countSubIslands(std::vector<std::vector<int>>& grid1, std::vector<std::vector<int>>& grid2) {
        int rows = (int)grid2.size(), cols = (int)grid2[0].size();
        std::function<bool(int, int)> dfs = [&](int r, int c) -> bool {
            if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0) return true;
            grid2[r][c] = 0;
            bool ok = grid1[r][c] == 1;
            if (!dfs(r + 1, c)) ok = false;
            if (!dfs(r - 1, c)) ok = false;
            if (!dfs(r, c + 1)) ok = false;
            if (!dfs(r, c - 1)) ok = false;
            return ok;
        };
        int ans = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid2[r][c] == 1 && dfs(r, c)) ans++;
            }
        }
        return ans;
    }
};
