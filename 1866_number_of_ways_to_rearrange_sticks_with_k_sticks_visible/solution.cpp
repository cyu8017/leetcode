// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

#include <vector>

class Solution {
public:
    int rearrangeSticks(int n, int k) {
        const int MOD = 1000000007;
        if (k == 0 || k > n) {
            return 0;
        }
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(n + 1, 0));
        dp[1][1] = 1;
        for (int sticks = 2; sticks <= n; sticks++) {
            dp[sticks][1] = (sticks - 1) * dp[sticks - 1][1] % MOD;
            for (int visible = 2; visible <= sticks; visible++) {
                dp[sticks][visible] = (dp[sticks - 1][visible - 1] + (sticks - 1) * dp[sticks - 1][visible]) % MOD;
            }
        }
        return static_cast<int>(dp[n][k]);
    }
};
