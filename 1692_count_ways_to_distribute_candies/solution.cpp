// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

#include <algorithm>
#include <vector>

class Solution {
public:
    int waysToDistribute(int n, int k) {
        const int MOD = 1000000007;
        std::vector<long long> dp(k + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; ++i) {
            for (int j = std::min(i, k); j >= 1; --j) {
                dp[j] = (dp[j - 1] + j * dp[j]) % MOD;
            }
            dp[0] = 0;
        }
        return static_cast<int>(dp[k]);
    }
};
