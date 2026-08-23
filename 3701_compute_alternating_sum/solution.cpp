// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

#include <vector>

class Solution {
public:
    int alternatingSum(std::vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i % 2 == 0) ans += nums[i];
            else ans -= nums[i];
        }
        return ans;
    }
};
