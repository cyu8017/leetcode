// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums) {
        for (int& x : nums) x *= x;
        std::sort(nums.begin(), nums.end());
        int m = (int)nums.size() / 2;
        long long ans = 0;
        for (int i = 0; i < m; i++) ans -= nums[i];
        for (int i = m; i < (int)nums.size(); i++) ans += nums[i];
        return ans;
    }
};
