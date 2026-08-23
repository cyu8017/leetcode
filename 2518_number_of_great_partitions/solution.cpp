// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

#include <vector>

class Solution {
public:
    int countPartitions(std::vector<int>& nums, int k) {
        const int MOD = 1000000007;
        long long sum = 0;
        for (int x : nums) sum += x;
        if (sum < 2LL * k) return 0;
        std::vector<int> dp(k);
        dp[0] = 1;
        for (int x : nums) {
            for (int s = k - 1; s >= x; s--) {
                dp[s] = (dp[s] + dp[s - x]) % MOD;
            }
        }
        int bad = 0;
        for (int v : dp) bad = (bad + v) % MOD;
        int total = 1;
        for (size_t i = 0; i < nums.size(); i++) total = total * 2 % MOD;
        return (total - 2LL * bad % MOD + MOD) % MOD;
    }
};
