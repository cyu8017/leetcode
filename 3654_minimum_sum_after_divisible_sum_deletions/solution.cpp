// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

#include <climits>
#include <vector>

class Solution {
public:
    long long minArraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = (prefix[i] + nums[i]) % k;
        const long long inf = 1LL << 62;
        std::vector<long long> dp(n + 1), best(k, inf);
        best[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + nums[i - 1];
            if (best[prefix[i]] < dp[i]) dp[i] = best[prefix[i]];
            if (dp[i] < best[prefix[i]]) best[prefix[i]] = dp[i];
        }
        return dp[n];
    }
};
