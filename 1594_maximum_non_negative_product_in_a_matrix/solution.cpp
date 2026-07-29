// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxProductPath(std::vector<std::vector<int>>& grid) {
        const int MOD = 1000000007;
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        std::vector<std::vector<long long>> high(m, std::vector<long long>(n));
        std::vector<std::vector<long long>> low(m, std::vector<long long>(n));
        high[0][0] = low[0][0] = grid[0][0];
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (r == 0 && c == 0) {
                    continue;
                }
                long long mx = LLONG_MIN;
                long long mn = LLONG_MAX;
                if (r > 0) {
                    mx = std::max({mx, high[r - 1][c] * grid[r][c], low[r - 1][c] * grid[r][c]});
                    mn = std::min({mn, high[r - 1][c] * grid[r][c], low[r - 1][c] * grid[r][c]});
                }
                if (c > 0) {
                    mx = std::max({mx, high[r][c - 1] * grid[r][c], low[r][c - 1] * grid[r][c]});
                    mn = std::min({mn, high[r][c - 1] * grid[r][c], low[r][c - 1] * grid[r][c]});
                }
                high[r][c] = mx;
                low[r][c] = mn;
            }
        }
        return high[m - 1][n - 1] >= 0 ? static_cast<int>(high[m - 1][n - 1] % MOD) : -1;
    }
};
