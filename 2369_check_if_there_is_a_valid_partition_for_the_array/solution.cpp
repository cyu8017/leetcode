// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

#include <vector>

class Solution {
public:
    bool validPartition(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<char> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            if (i >= 2 && nums[i - 1] == nums[i - 2] && dp[i - 2]) dp[i] = 1;
            if (i >= 3 && nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3]) dp[i] = 1;
            if (i >= 3 && nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3]) dp[i] = 1;
        }
        return dp[n];
    }
};
