// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

#include <vector>
#include <unordered_map>

class Solution {
    std::vector<std::vector<int>> rotate(const std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> t(n, std::vector<int>(m));
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) t[j][i] = grid[i][j];
        return t;
    }
    bool check(const std::vector<std::vector<int>>& g) {
        int m = (int)g.size(), n = (int)g[0].size();
        long long s1 = 0, s2 = 0;
        std::unordered_map<long long, int> cnt1, cnt2;
        for (auto& row : g) for (int x : row) {
            long long v = x;
            s2 += v;
            cnt2[v]++;
        }
        for (int i = 0; i < m - 1; i++) {
            for (int x : g[i]) {
                long long v = x;
                s1 += v; s2 -= v;
                cnt1[v]++; cnt2[v]--;
            }
            if (s1 == s2) return true;
            if (s1 < s2) {
                long long diff = s2 - s1;
                if (cnt2[diff] > 0) {
                    if ((m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                        (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff)))
                        return true;
                }
            } else {
                long long diff = s1 - s2;
                if (cnt1[diff] > 0) {
                    if ((i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                        (n == 1 && (g[0][0] == diff || g[i][0] == diff)))
                        return true;
                }
            }
        }
        return false;
    }
public:
    bool canPartitionGrid(std::vector<std::vector<int>>& grid) {
        return check(grid) || check(rotate(grid));
    }
};
