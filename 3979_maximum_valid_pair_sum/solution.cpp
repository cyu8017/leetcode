// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxValidPairSum(std::vector<int>& nums, int k) {
        int ans = 0, x = 0;
        for (int j = k; j < (int)nums.size(); j++) {
            int y = nums[j];
            x = std::max(x, nums[j - k]);
            ans = std::max(ans, x + y);
        }
        return ans;
    }
};
