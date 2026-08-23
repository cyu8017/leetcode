// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

#include <vector>

class Solution {
public:
    std::vector<long long> resultArray(std::vector<int>& nums, int k) {
        std::vector<long long> ans(k), dp(k);
        for (int num : nums) {
            std::vector<long long> newDp(k);
            int nm = num % k;
            newDp[nm] = 1;
            for (int i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
            for (int i = 0; i < k; i++) ans[i] += newDp[i];
            dp.swap(newDp);
        }
        return ans;
    }
};
