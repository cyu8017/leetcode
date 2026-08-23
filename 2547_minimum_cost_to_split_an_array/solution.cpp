// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minCost(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const long long INF = (long long)1e18;
        std::vector<long long> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            std::unordered_map<int, int> freq;
            int trimmed = 0;
            for (int j = i; j < n; ++j) {
                int c = ++freq[nums[j]];
                if (c == 2) trimmed += 2;
                else if (c > 2) trimmed++;
                long long cost = dp[i] + k + trimmed;
                if (cost < dp[j + 1]) dp[j + 1] = cost;
            }
        }
        return (int)dp[n];
    }
};
