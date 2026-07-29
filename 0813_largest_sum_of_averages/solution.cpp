// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

#include <algorithm>
#include <vector>

class Solution {
public:
    double largestSumOfAverages(std::vector<int>& nums, int k) {
        int n = static_cast<int>(nums.size());
        std::vector<double> prefix(n + 1, 0.0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        auto average = [&](int i, int j) {
            return (prefix[j] - prefix[i]) / (j - i);
        };
        std::vector<double> dp(n);
        for (int i = 0; i < n; ++i) {
            dp[i] = average(0, i + 1);
        }
        for (int groups = 2; groups <= k; ++groups) {
            std::vector<double> nxt(n, 0.0);
            for (int i = groups - 1; i < n; ++i) {
                double best = 0.0;
                for (int j = groups - 2; j < i; ++j) {
                    best = std::max(best, dp[j] + average(j + 1, i + 1));
                }
                nxt[i] = best;
            }
            dp.swap(nxt);
        }
        return dp[n - 1];
    }
};
