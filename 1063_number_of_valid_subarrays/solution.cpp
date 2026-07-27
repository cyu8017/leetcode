// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

#include <vector>

class Solution {
public:
    int validSubarrays(std::vector<int>& nums) {
        std::vector<int> stack;
        int ans = 0;
        int n = static_cast<int>(nums.size());
        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && nums[stack.back()] > nums[i]) {
                int j = stack.back();
                stack.pop_back();
                ans += i - j;
            }
            stack.push_back(i);
        }
        while (!stack.empty()) {
            int j = stack.back();
            stack.pop_back();
            ans += n - j;
        }
        return ans;
    }
};
