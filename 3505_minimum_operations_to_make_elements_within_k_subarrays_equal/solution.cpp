// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int x, int k) {
        int n = (int)nums.size();
        std::vector<long long> minOps(n - x + 1);
        for (int i = 0; i + x <= n; i++) {
            std::vector<int> w(nums.begin() + i, nums.begin() + i + x);
            std::sort(w.begin(), w.end());
            int med = w[(x - 1) / 2];
            long long ops = 0;
            for (int v : w) ops += std::abs(v - med);
            minOps[i] = ops;
        }
        const long long inf = 1LL << 62;
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(k + 1, inf));
        dp[n][0] = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = dp[i + 1][j];
                if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                    dp[i][j] = minOps[i] + dp[i + x][j - 1];
            }
        }
        return dp[0][k];
    }
};
