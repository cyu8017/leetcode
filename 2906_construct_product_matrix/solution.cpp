// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> constructProductMatrix(std::vector<std::vector<int>>& grid) {
        const int mod = 12345;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        int pref = 1;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                ans[i][j] = pref;
                pref = 1LL * pref * (grid[i][j] % mod) % mod;
            }
        int suf = 1;
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                ans[i][j] = 1LL * ans[i][j] * suf % mod;
                suf = 1LL * suf * (grid[i][j] % mod) % mod;
            }
        return ans;
    }
};
