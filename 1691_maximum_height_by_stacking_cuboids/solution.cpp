// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxHeight(std::vector<std::vector<int>>& cuboids) {
        for (auto& c : cuboids) {
            std::sort(c.begin(), c.end());
        }
        std::sort(cuboids.begin(), cuboids.end());
        int n = static_cast<int>(cuboids.size());
        std::vector<int> dp(n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            dp[i] = cuboids[i][2];
            for (int j = 0; j < i; ++j) {
                if (cuboids[j][0] <= cuboids[i][0] && cuboids[j][1] <= cuboids[i][1] &&
                    cuboids[j][2] <= cuboids[i][2]) {
                    dp[i] = std::max(dp[i], dp[j] + cuboids[i][2]);
                }
            }
            ans = std::max(ans, dp[i]);
        }
        return ans;
    }
};
