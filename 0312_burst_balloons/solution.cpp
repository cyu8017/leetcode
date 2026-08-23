// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxCoins(std::vector<int>& nums) {
        std::vector<int> balloons;
        balloons.push_back(1);
        balloons.insert(balloons.end(), nums.begin(), nums.end());
        balloons.push_back(1);

        int size = static_cast<int>(balloons.size());
        std::vector<std::vector<int>> dp(size, std::vector<int>(size, 0));

        for (int length = 3; length <= size; length++) {
            for (int left = 0; left <= size - length; left++) {
                int right = left + length - 1;
                for (int mid = left + 1; mid < right; mid++) {
                    int coins = dp[left][mid]
                        + dp[mid][right]
                        + balloons[left] * balloons[mid] * balloons[right];
                    dp[left][right] = std::max(dp[left][right], coins);
                }
            }
        }

        return dp[0][size - 1];
    }
};
