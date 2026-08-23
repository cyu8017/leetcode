// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

#include <vector>

class Solution {
public:
    bool predictTheWinner(std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[i][i] = nums[i];
        }
        for (int length = 2; length <= n; ++length) {
            for (int left = 0; left + length - 1 < n; ++left) {
                const int right = left + length - 1;
                dp[left][right] = std::max(
                    nums[left] - dp[left + 1][right],
                    nums[right] - dp[left][right - 1]);
            }
        }
        return dp[0][n - 1] >= 0;
    }
};
