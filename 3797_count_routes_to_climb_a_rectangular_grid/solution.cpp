// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    int countRoutes(std::vector<std::string>& grid, int d) {
        const int MOD = 1000000007;
        int n = (int)grid.size(), m = (int)grid[0].size();
        int upRadius = 0;
        while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) upRadius++;
        std::vector<int> arrived(m, 0);
        for (int c = 0; c < m; c++) {
            if (grid[n - 1][c] == '.') arrived[c] = 1;
        }
        auto rowWays = [&](int row, const std::vector<int>& base) {
            std::vector<int> pref(m + 1, 0);
            for (int i = 0; i < m; i++) pref[i + 1] = (pref[i] + base[i]) % MOD;
            std::vector<int> horizontal(m, 0);
            for (int c = 0; c < m; c++) {
                if (grid[row][c] == '#') continue;
                int l = std::max(0, c - d), r = std::min(m - 1, c + d);
                horizontal[c] = (pref[r + 1] - pref[l] - base[c]) % MOD;
                if (horizontal[c] < 0) horizontal[c] += MOD;
            }
            return std::make_pair(base, horizontal);
        };
        for (int r = n - 1; r >= 0; r--) {
            auto [base, horizontal] = rowWays(r, arrived);
            if (r == 0) {
                int ans = 0;
                for (int c = 0; c < m; c++) ans = (ans + base[c] + horizontal[c]) % MOD;
                return ans;
            }
            std::vector<int> pref(m + 1, 0);
            for (int c = 0; c < m; c++) pref[c + 1] = (pref[c] + base[c] + horizontal[c]) % MOD;
            std::vector<int> next(m, 0);
            for (int c = 0; c < m; c++) {
                if (grid[r - 1][c] == '#') continue;
                int l = std::max(0, c - upRadius), rr = std::min(m - 1, c + upRadius);
                next[c] = pref[rr + 1] - pref[l];
                if (next[c] < 0) next[c] += MOD;
            }
            arrived = std::move(next);
        }
        return 0;
    }
};
