// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

#include <vector>

class Solution {
public:
    int countPathsWithXorValue(std::vector<std::vector<int>>& grid, int k) {
        const int mod = 1000000007;
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<std::vector<int>>> dp(m, std::vector<std::vector<int>>(n, std::vector<int>(16, 0)));
        dp[0][0][grid[0][0]] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int x = 0; x < 16; x++) {
                    if (dp[i][j][x] == 0) continue;
                    if (i + 1 < m) {
                        int nx = x ^ grid[i + 1][j];
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod;
                    }
                    if (j + 1 < n) {
                        int nx = x ^ grid[i][j + 1];
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k];
    }
};
