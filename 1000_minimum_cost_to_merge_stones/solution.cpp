// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int mergeStones(std::vector<int>& stones, int k) {
        int n = static_cast<int>(stones.size());
        if ((n - 1) % (k - 1) != 0) return -1;
        std::vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + stones[i];
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int length = k; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                dp[i][j] = INT_MAX;
                for (int m = i; m < j; m += k - 1) {
                    dp[i][j] = std::min(dp[i][j], dp[i][m] + dp[m + 1][j]);
                }
                if ((length - 1) % (k - 1) == 0) {
                    dp[i][j] += prefix[j + 1] - prefix[i];
                }
            }
        }
        return dp[0][n - 1];
    }
};

