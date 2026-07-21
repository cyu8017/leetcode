// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    std::vector<int> getBiggestThree(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::vector<std::vector<int>> s1(m + 1, std::vector<int>(n + 2, 0));
        std::vector<std::vector<int>> s2(m + 1, std::vector<int>(n + 2, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                s1[i][j] = s1[i - 1][j - 1] + value;
                s2[i][j] = s2[i - 1][j + 1] + value;
            }
        }

        std::set<int> rhombusSums;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int value = grid[i - 1][j - 1];
                int limit = std::min({i - 1, m - i, j - 1, n - j});
                rhombusSums.insert(value);
                for (int k = 1; k <= limit; k++) {
                    int a = s1[i + k][j] - s1[i][j - k];
                    int b = s1[i][j + k] - s1[i - k][j];
                    int c = s2[i][j - k] - s2[i - k][j];
                    int d = s2[i + k][j] - s2[i][j + k];
                    rhombusSums.insert(a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]);
                }
            }
        }

        std::vector<int> result(rhombusSums.rbegin(), rhombusSums.rend());
        if (result.size() > 3) {
            result.resize(3);
        }
        return result;
    }
};
