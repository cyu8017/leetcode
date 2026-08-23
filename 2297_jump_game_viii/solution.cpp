// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

#include <vector>
#include <climits>
#include <algorithm>

class Solution {
public:
    long long minCost(std::vector<int>& nums, std::vector<int>& costs) {
        int n = (int)nums.size();
        std::vector<long long> dp(n, LLONG_MAX / 4);
        dp[0] = 0;
        std::vector<int> stack1, stack2;
        for (int i = 0; i < n; ++i) {
            while (!stack1.empty() && nums[stack1.back()] <= nums[i]) {
                int j = stack1.back(); stack1.pop_back();
                dp[i] = std::min(dp[i], dp[j] + costs[i]);
            }
            while (!stack2.empty() && nums[stack2.back()] > nums[i]) {
                int j = stack2.back(); stack2.pop_back();
                dp[i] = std::min(dp[i], dp[j] + costs[i]);
            }
            if (!stack1.empty()) dp[i] = std::min(dp[i], dp[stack1.back()] + costs[i]);
            if (!stack2.empty()) dp[i] = std::min(dp[i], dp[stack2.back()] + costs[i]);
            stack1.push_back(i);
            stack2.push_back(i);
        }
        return dp[n - 1];
    }
};
