// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int k, int m) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        const long long neg = (long long)(-1LL << 60);
        std::vector<std::vector<long long>> dp(k + 1, std::vector<long long>(n + 1, neg));
        for (int i = 0; i <= n; i++) dp[0][i] = 0;
        for (int t = 1; t <= k; t++) {
            long long best = neg;
            for (int i = t * m; i <= n; i++) {
                int j = i - m;
                best = std::max(best, dp[t - 1][j] - pref[j]);
                dp[t][i] = best + pref[i];
            }
            for (int i = 1; i <= n; i++) dp[t][i] = std::max(dp[t][i], dp[t][i - 1]);
        }
        return dp[k][n];
    }
};
