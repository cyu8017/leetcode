// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int movesToMakeZigzag(std::vector<int>& nums) {
        auto cost = [&](int start) {
            int ans = 0;
            for (int i = start; i < static_cast<int>(nums.size()); i += 2) {
                int left = i ? nums[i - 1] : INT_MAX;
                int right = i + 1 < static_cast<int>(nums.size()) ? nums[i + 1] : INT_MAX;
                ans += std::max(0, nums[i] - std::min(left, right) + 1);
            }
            return ans;
        };
        return std::min(cost(0), cost(1));
    }
};
