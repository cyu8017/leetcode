// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

#include <algorithm>
#include <vector>

class Solution {
public:
    int wiggleMaxLength(std::vector<int>& nums) {
        if (nums.size() < 2) {
            return static_cast<int>(nums.size());
        }

        int up = 1;
        int down = 1;
        for (size_t index = 1; index < nums.size(); ++index) {
            if (nums[index] > nums[index - 1]) {
                up = down + 1;
            } else if (nums[index] < nums[index - 1]) {
                down = up + 1;
            }
        }

        return std::max(up, down);
    }
};
