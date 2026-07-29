// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

#include <vector>

class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1000000007;
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));
        dp[startRow][startColumn] = 1;
        int result = 0;
        const int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int move = 0; move < maxMove; ++move) {
            std::vector<std::vector<int>> nxt(m, std::vector<int>(n, 0));
            for (int row = 0; row < m; ++row) {
                for (int col = 0; col < n; ++col) {
                    int ways = dp[row][col];
                    if (ways == 0) {
                        continue;
                    }
                    for (int d = 0; d < 4; ++d) {
                        int nr = row + dirs[d][0];
                        int nc = col + dirs[d][1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                            nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD;
                        } else {
                            result = (result + ways) % MOD;
                        }
                    }
                }
            }
            dp = std::move(nxt);
        }
        return result;
    }
};
