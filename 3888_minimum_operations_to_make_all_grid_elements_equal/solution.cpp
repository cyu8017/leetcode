// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int maxVal = grid[0][0];
        for (auto& row : grid) {
            maxVal = std::max(maxVal, *std::max_element(row.begin(), row.end()));
        }

        auto check = [&](int target) -> long long {
            std::vector<std::vector<long long>> diff(m + 2, std::vector<long long>(n + 2, 0));
            long long totalOps = 0;
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                    long long curVal = (long long)grid[i - 1][j - 1] + diff[i][j];
                    if (curVal > target) return -1;
                    if (curVal < target) {
                        if (i + k - 1 > m || j + k - 1 > n) return -1;
                        long long needed = target - curVal;
                        totalOps += needed;
                        diff[i][j] += needed;
                        diff[i + k][j] -= needed;
                        diff[i][j + k] -= needed;
                        diff[i + k][j + k] += needed;
                    }
                }
            }
            return totalOps;
        };

        for (int t = maxVal; t <= maxVal + 1; t++) {
            long long res = check(t);
            if (res != -1) return res;
        }
        return -1;
    }
};
