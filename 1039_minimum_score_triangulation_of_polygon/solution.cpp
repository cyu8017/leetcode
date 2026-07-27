// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

#include <climits>
#include <vector>

class Solution {
public:
    int minScoreTriangulation(std::vector<int>& values) {
        int n = static_cast<int>(values.size());
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int len = 2; len < n; ++len) {
            for (int i = 0; i + len < n; ++i) {
                int j = i + len;
                dp[i][j] = INT_MAX;
                for (int k = i + 1; k < j; ++k) {
                    dp[i][j] = std::min(dp[i][j],
                                        dp[i][k] + values[i] * values[k] * values[j] + dp[k][j]);
                }
            }
        }
        return dp[0][n - 1];
    }
};

