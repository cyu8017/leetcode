// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums) {
        long long ans = 0;
        for (int i = 1; i < (int)nums.size(); i++) {
            ans += std::max(0LL, (long long)nums[i - 1] - nums[i]);
        }
        return ans;
    }
};
