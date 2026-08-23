// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

#include <algorithm>
#include <array>
#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        const int INF = 1 << 30;
        std::vector<std::array<int, 4>> dp(n + 1);
        for (int i = 0; i <= n; i++) for (int g = 1; g <= 3; g++) dp[i][g] = INF;
        dp[0][1] = dp[0][2] = dp[0][3] = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            for (int g = 1; g <= 3; g++) {
                int cost = (v != g);
                for (int prev = 1; prev <= g; prev++)
                    dp[i][g] = std::min(dp[i][g], dp[i - 1][prev] + cost);
            }
        }
        return std::min({dp[n][1], dp[n][2], dp[n][3]});
    }
};
