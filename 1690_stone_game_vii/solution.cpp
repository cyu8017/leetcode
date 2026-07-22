// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int stoneGameVII(std::vector<int>& stones) {
        int n = static_cast<int>(stones.size());
        std::vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = pre[i] + stones[i];
        }
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int length = 2; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                dp[i][j] = std::max(pre[j + 1] - pre[i + 1] - dp[i + 1][j], pre[j] - pre[i] - dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }
};
