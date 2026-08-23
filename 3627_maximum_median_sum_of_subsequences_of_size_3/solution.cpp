// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maximumMedianSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = n / 3; i < n; i += 2) ans += nums[i];
        return ans;
    }
};
