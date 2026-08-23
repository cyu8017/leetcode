// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxWidthRamp(std::vector<int>& nums) {
        std::vector<int> stack;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (stack.empty() || nums[stack.back()] > nums[i]) stack.push_back(i);
        }
        int ans = 0;
        for (int j = (int)nums.size() - 1; j >= 0; j--) {
            while (!stack.empty() && nums[stack.back()] <= nums[j]) {
                ans = std::max(ans, j - stack.back());
                stack.pop_back();
            }
        }
        return ans;
    }
};
