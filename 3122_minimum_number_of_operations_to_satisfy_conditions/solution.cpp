// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

#include <vector>
#include <algorithm>
#include <array>

class Solution {
public:
    int minimumOperations(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        const int inf = 1 << 29;
        std::vector<std::vector<int>> f(n, std::vector<int>(10, inf));
        for (int i = 0; i < n; i++) {
            std::array<int, 10> cnt{};
            for (int j = 0; j < m; j++) cnt[grid[j][i]]++;
            if (i == 0) {
                for (int j = 0; j < 10; j++) f[i][j] = m - cnt[j];
            } else {
                for (int j = 0; j < 10; j++) {
                    for (int k = 0; k < 10; k++) {
                        if (j != k) f[i][j] = std::min(f[i][j], f[i - 1][k] + m - cnt[j]);
                    }
                }
            }
        }
        return *std::min_element(f[n - 1].begin(), f[n - 1].end());
    }
};
