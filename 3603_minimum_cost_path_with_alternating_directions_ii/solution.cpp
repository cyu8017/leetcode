// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minCost(int m, int n, std::vector<std::vector<int>>& waitCost) {
        std::vector<std::vector<long long>> dp(m, std::vector<long long>(n, LLONG_MAX / 4));
        auto entry = [](int i, int j) { return 1LL * (i + 1) * (j + 1); };
        dp[0][0] = entry(0, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (i > 0) {
                    long long cand = dp[i - 1][j] + entry(i, j);
                    if (!(i - 1 == 0 && j == 0)) cand += waitCost[i - 1][j];
                    dp[i][j] = std::min(dp[i][j], cand);
                }
                if (j > 0) {
                    long long cand = dp[i][j - 1] + entry(i, j);
                    if (!(i == 0 && j - 1 == 0)) cand += waitCost[i][j - 1];
                    dp[i][j] = std::min(dp[i][j], cand);
                }
            }
        }
        return dp[m - 1][n - 1];
    }
};
